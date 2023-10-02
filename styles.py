"""styles"""


def get_styles(style_file='default.css'):
    with open(style_file, 'r') as f:
        return f.read()


def make_header(styles=None):
    return """<head>
      <meta charset="utf-8"> <!-- utf-8 works for most cases -->
    <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
    <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
    <meta name="format-detection" content="telephone=no,address=no,email=no,date=no,url=no"> <!-- Tell iOS not to automatically link certain text strings. -->
    <meta name="color-scheme" content="light">
    <meta name="supported-color-schemes" content="light">
    <!-- What it does: Makes background images in 72ppi Outlook render at correct size. -->
    <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
  <title></title><style>
  
  """ + get_styles() + """\n\n   </style> </head>"""


DEFAULT_HEADER = """<html>



  <style>
body {
  font-family: Helvetica, sans-serif;
  font-size: 14px;
}
.content {
  background-color: white;
}
.content .message-block {
  margin-bottom: 24px;
}
.header .message-block, .footer message-block {
  margin-bottom: 12px;
}
img {
  max-width: 100%;
  padding: 5px;
}

p{
    padding 0px;
}

figcaption {

margin-top: 1em;

}

@media only screen and (max-width: 767px) {
  .container {
    width: 100%;
  }
  .articles, .articles tr, .articles td {
    display: block;
    width: 100%;
  }
  .article {
    margin-bottom: 24px;
  }
}

table {
        margin-left: auto;
        margin-right: auto;
        border: none;
        width: auto;
        border-collapse: collapse;
        border-spacing: 0;
        color: @rendered_html_border_color;
        font-size: 16px;
        table-layout: fixed;
    }
    thead {
        border-bottom: 1px solid @rendered_html_border_color;
        vertical-align: bottom;
    }
    tr, th, td {
        text-align: right;
        vertical-align: middle;
        padding: 0.5em 0.5em;
        line-height: normal;
        white-space: normal;
        max-width: none;
        border: none;
    }
    th {
        font-weight: bold;
    }
    tbody tr:nth-child(odd) {
        background: #f5f5f5;
    }
    tbody tr:hover {
        background: rgba(66, 165, 245, 0.2);
    }


      </style>
  </head>
  
  """
