DEFAULT_HEADER = """<html><head><style>
    
    img {
        margin: 0 auto;
        display: block;
        width: 80%;
    }

    h1, h2, h3, h4, h5 {
    
    text-align: center;
    
    }

    p

    {
    font-size: 1.3em;

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
    


    </style></head>"""
