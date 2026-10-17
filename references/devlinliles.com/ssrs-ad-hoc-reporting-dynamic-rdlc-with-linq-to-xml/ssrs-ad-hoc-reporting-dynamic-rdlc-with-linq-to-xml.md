---
type: Reference
title: "SSRS Ad-Hoc Reporting: Dynamic RDLC with LINQ to XML"
resource: "https://www.devlinliles.com/ssrs-ad-hoc-reporting-dynamic-rdlc-with-linq-to-xml/"
author: "Devlin Liles"
published: '2026-06-08'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I ran into a couple of different issues when setting up advanced reporting scenarios with SQL Server Reporting Services. While SSRS runs fairly well in server-report situations, it lacks flexibility in application integration scenarios. Having to hard-code datasets for each report and hard-code fill/get methods seemed inelegant. I wanted a more robust solution — so I came up with an approach that lets me take preset report segments and load them dynamically into a report definition before passing it to the renderer.

## The Approach

You start by setting up a blank RDLC with a header and footer. This keeps formatting consistent throughout the report. You can use global variables or parameters in the header and footer — most of the time these will be standard for the application and templated for the company.

## Loading the RDLC

Load the RDLC from a file stream into an `XDocument`:

```csharp
private Stream Load_FileStream()
{
    Stream MasterReport = new FileStream(
        Server.MapPath("~/Report/Master.rdlc"),
        FileMode.Open,
        FileAccess.Read);
    return MasterReport;
}
```

## Finding the Body's ReportItems Node

Using LINQ you can search the nodes for the `ReportItems` node in the body — this is where the guts of the report live:

```csharp
private Stream PrepReport()
{
    XDocument ReportDoc = XDocument.Load(XmlReader.Create(Load_FileStream()));
    IEnumerable<XNode> hold = ReportDoc.DescendantNodes().InDocumentOrder();
    XElement BodyItems = (XElement)hold.Where(n =>
        n.GetType() != typeof(XText) &&
        ((XElement)n).Parent != null &&
        ((XElement)n).Name.LocalName.ToUpper() == "REPORTITEMS" &&
        ((XElement)n).Parent.Name.LocalName.ToUpper() == "BODY").SingleOrDefault();

    BodyItems.Add(NewNodes(ReportDoc.Root.Name.Namespace));
    return CreateMemoryStream(ReportDoc);
}
```

## Inserting a Sub-Report Node

Use LINQ to XML to insert a new node package to add tables, sub-reports, or graphs. In this example I add a sub-report with a parameter:

```csharp
private XElement NewNodes(XNamespace @namespace)
{
    var holder = new XElement(@namespace + "Subreport",
        new object[] {
            new XAttribute("Name", "Subreport1"),
            new XElement(@namespace + "Parameters",
                new XElement(@namespace + "Parameter",
                    new object[] {
                        new XElement(@namespace + "Value", "=Parameter!Period.Value"),
                        new XAttribute("Name", "Period")
                    })),
            new XElement(@namespace + "ReportName", "NameHere"),
            new XElement(@namespace + "Top", "0.25in"),
            new XElement(@namespace + "Width", "7.25in"),
            new XElement(@namespace + "Left", "0.125in"),
            new XElement(@namespace + "Height", "0.25in")
        });
    return holder;
}
```

The width value changes for paper orientation, and the top changes based on how many reports you insert. The height is set to a quarter inch because sub-reports auto-expand to their content.

## Packaging to a Memory Stream

```csharp
private Stream CreateMemoryStream(XDocument doc)
{
    MemoryStream memStream = new MemoryStream();
    XmlWriter writer = XmlWriter.Create(memStream);
    if (writer != null)
    {
        doc.Save(writer);
        writer.Close();
    }
    memStream.Position = 0;
    return memStream;
}
```

Make sure you reset the position — if you don't, the read will start at the end and give an invalid RDLC error. Once packaged, you wire it to the `ReportViewer` control the same way you would with a static report:

```csharp
private void GenerateReport()
{
    ReportViewer1.LocalReport.LoadReportDefinition(PrepReport());
    ReportViewer1.LocalReport.DisplayName = "Set what you want the export file name to be.";
    ReportViewer1.LocalReport.LoadSubreportDefinition("SubReport",
        new FileStream(Server.MapPath("~/Report/Subreport.rdlc"),
            FileMode.Open, FileAccess.Read));
    ReportViewer1.ReportError += ReportError;
    ReportViewer1.LocalReport.SubreportProcessing += LocalReport_SubreportProcessing;
    ReportViewer1.LocalReport.Refresh();
    ReportViewer1.ZoomMode = ZoomMode.PageWidth;
    ReportViewer1.Focus();
}

private void LocalReport_SubreportProcessing(object sender,
    Microsoft.Reporting.WebForms.SubreportProcessingEventArgs e)
{
    // Provide the data sources for your sub-reports here
    e.DataSources.Add(new ReportDataSource("Something", "MethodCallHere"));
}

private void ReportError(object sender,
    Microsoft.Reporting.WebForms.ReportErrorEventArgs e)
{
    // Error handling and report logging here
}
```

This provides the basis for an ad-hoc report integration. Happy coding, and remember to code like you have to support it.

## Full Code Sample

The complete `_Default` page class putting all of the above together:

```csharp
public class _Default : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
    }

    private Stream Load_FileStream()
    {
        var MasterReport = new FileStream(
            Server.MapPath("~/Report/Master.rdlc"),
            FileMode.Open, FileAccess.Read);
        return MasterReport;
    }

    private Stream PrepReport()
    {
        XDocument ReportDoc = XDocument.Load(XmlReader.Create(Load_FileStream()));
        IEnumerable<XNode> hold = ReportDoc.DescendantNodes().InDocumentOrder();
        var BodyItems = (XElement)hold.Where(
            n =>
            n.GetType() != typeof(XText) &&
            ((XElement)n).Parent != null &&
            ((XElement)n).Name.LocalName.ToUpper() == "REPORTITEMS" &&
            ((XElement)n).Parent.Name.LocalName.ToUpper() == "BODY").SingleOrDefault();
        BodyItems.Add(NewNodes(ReportDoc.Root.Name.Namespace));
        return CreateMemoryStream(ReportDoc);
    }

    private XElement NewNodes(XNamespace @namespace)
    {
        var holder = new XElement(@namespace + "Subreport",
            new object[]
            {
                new XAttribute("Name", "Subreport1"),
                new XElement(@namespace + "Parameters",
                    new XElement(@namespace + "Parameter",
                        new object[]
                        {
                            new XElement(@namespace + "Value", "=Parameter!Period.Value"),
                            new XAttribute("Name", "Period")
                        })),
                new XElement(@namespace + "ReportName", "NameHere"),
                new XElement(@namespace + "Top", "0.25in"),
                new XElement(@namespace + "Width", "7.25in"),
                new XElement(@namespace + "Left", "0.125in"),
                new XElement(@namespace + "Height", "0.25in")
            });
        return holder;
    }

    private Stream CreateMemoryStream(XDocument doc)
    {
        var memStream = new MemoryStream();
        XmlWriter writer = XmlWriter.Create(memStream);
        if (writer != null)
        {
            doc.Save(writer);
            writer.Close();
        }
        memStream.Position = 0;
        return memStream;
    }

    private void GenerateReport()
    {
        ReportViewer1.LocalReport.LoadReportDefinition(PrepReport());
        ReportViewer1.LocalReport.DisplayName = "Set what you want the export file name to be.";
        ReportViewer1.LocalReport.LoadSubreportDefinition("SubReport",
            new FileStream(
                Server.MapPath("~/Report/Subreport.rdlc"),
                FileMode.Open, FileAccess.Read));
        ReportViewer1.ReportError += ReportError;
        ReportViewer1.LocalReport.SubreportProcessing += LocalReport_SubreportProcessing;
        ReportViewer1.LocalReport.Refresh();
        ReportViewer1.ZoomMode = ZoomMode.PageWidth;
        ReportViewer1.Focus();
    }

    private void LocalReport_SubreportProcessing(object sender,
        Microsoft.Reporting.WebForms.SubreportProcessingEventArgs e)
    {
        // Provide the data sources for your sub-reports here
        e.DataSources.Add(new ReportDataSource("Something", "MethodCallHere"));
    }

    private void ReportError(object sender,
        Microsoft.Reporting.WebForms.ReportErrorEventArgs e)
    {
        // Error handling and report logging here
    }
}
```
