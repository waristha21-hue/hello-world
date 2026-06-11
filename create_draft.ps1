$ol = New-Object -ComObject Outlook.Application
$mail = $ol.CreateItem(0)

# To / CC
$mail.To = "chanutthaporn_diag@meditopthailand.com"
$mail.CC = "suchart_diag@meditopthailand.com; waristha_diag@meditopthailand.com"

# Subject
$mail.Subject = [string]::Join("", @("รบกวนใบเสนอราคาสินค้า RANDOX RIQAS ของ โรงพยาบาลราชพิพัฒน์"))

# Embed logo
$logoPath = "C:\Users\ACER\Desktop\claude\hello-world\signature_logo.png"
$logoAtt = $mail.Attachments.Add($logoPath, 1, 0, "signature_logo")
$pr = "http://schemas.microsoft.com/mapi/proptag/0x3712001F"
$logoAtt.PropertyAccessor.SetProperty($pr, "image001.png")

# HTML Body - exact format from original email
$mail.HTMLBody = @'
<html><head>
<style>
p.MsoNormal, li.MsoNormal, div.MsoNormal {
    margin:0cm;
    font-size:16.0pt;
    font-family:"Cordia New",sans-serif;
}
</style>
</head>
<body lang=EN-US style='word-wrap:break-word'>
<div class=WordSection1>
<p class=MsoNormal><span style='font-family:"DilleniaUPC",serif'>&#x0E40;&#x0E23;&#x0E35;&#x0E22;&#x0E19;&#x0E1E;&#x0E35;&#x0E48;&#x0E0A;&#x0E21;&#x0E1E;&#x0E39;&#x0E48;,</span></p>
<p class=MsoNormal><span style='font-family:"DilleniaUPC",serif'>&#x0E23;&#x0E1A;&#x0E01;&#x0E27;&#x0E19;&#x0E43;&#x0E1A;&#x0E40;&#x0E2A;&#x0E19;&#x0E2D;&#x0E23;&#x0E32;&#x0E04;&#x0E32;&#x0E2A;&#x0E34;&#x0E19;&#x0E04;&#x0E49;&#x0E32; RANDOX RIQAS &#x0E02;&#x0E2D;&#x0E07; &#x0E42;&#x0E23;&#x0E07;&#x0E1E;&#x0E22;&#x0E32;&#x0E1A;&#x0E32;&#x0E25;&#x0E23;&#x0E32;&#x0E0A;&#x0E1E;&#x0E34;&#x0E1E;&#x0E31;&#x0E12;&#x0E19;&#x0E4C; &#x0E04;&#x0E48;&#x0E30;</span></p>
<p class=MsoNormal><span style='font-family:"DilleniaUPC",serif'>&#x0E23;&#x0E32;&#x0E22;&#x0E01;&#x0E32;&#x0E23;: RDX-RQ9128 RIQAS Monthly Chemistry Programme</span></p>
<p class=MsoNormal><span style='font-family:"DilleniaUPC",serif'>Cycle 24A, 24B (&#x0E21;.&#x0E04;.2027 - &#x0E18;.&#x0E04;.2027)</span></p>
<p class=MsoNormal><span style='font-family:"DilleniaUPC",serif'>&nbsp;</span></p>
<p class=MsoNormal><span style='font-family:"DilleniaUPC",serif'>&nbsp;</span></p>
<div>
<p class=MsoNormal><b><span style='font-size:14.0pt;font-family:"DilleniaUPC",serif'>&#x0E02;&#x0E2D;&#x0E1A;&#x0E1E;&#x0E23;&#x0E30;&#x0E04;&#x0E38;&#x0E13;&#x0E40;&#x0E1B;&#x0E47;&#x0E19;&#x0E2D;&#x0E22;&#x0E48;&#x0E32;&#x0E07;&#x0E2A;&#x0E39;&#x0E07;&#x0E04;&#x0E48;&#x0E30;</span></b></p>
<p class=MsoNormal><b><span style='font-size:14.0pt;font-family:"DilleniaUPC",serif'>&#x0E27;&#x0E23;&#x0E34;&#x0E29;&#x0E10;&#x0E32; &nbsp;&#x0E0B;&#x0E34;&#x0E49;&#x0E21;&#x0E28;&#x0E34;&#x0E23;&#x0E34;&#x0E1E;&#x0E23;</span></b></p>
<p class=MsoNormal><span style='font-size:14.0pt;font-family:"DilleniaUPC",serif'>&nbsp;</span></p>
<p class=MsoNormal><b><span style='font-size:14.0pt;font-family:"DilleniaUPC",serif'>Best Regards,</span></b></p>
<p class=MsoNormal><span style='font-size:14.0pt'><img width=151 height=115 src="cid:image001.png"></span></p>
<p class=MsoNormal><b><span style='font-size:14.0pt'>Ms. Waristha &nbsp;Simsiriporn (N&#39;Job)</span></b></p>
<p class=MsoNormal><span style='font-size:14.0pt'>Sales Representative</span></p>
<p class=MsoNormal><span style='font-size:14.0pt'>Diagnostics Division</span></p>
<p class=MsoNormal><span style='font-size:14.0pt'>Meditop Co.,Ltd.</span></p>
<p class=MsoNormal><span style='font-size:14.0pt'>Mob. +666 1386 6575</span></p>
<p class=MsoNormal><span style='font-size:14.0pt'>E-mail : <a href="mailto:waristha_diag@meditopthailand.com">waristha_diag@meditopthailand.com</a></span></p>
<p class=MsoNormal><span style='font-size:14.0pt'><a href="http://www.meditopthailand.com/">www.meditopthailand.com</a></span></p>
</div>
</div></body></html>
'@

# Attach quotation Excel
$mail.Attachments.Add("C:\Users\ACER\Desktop\ใบเสนอราคา_ราชพิพัฒน์_RIQAS_RQ9128.xlsx")

# Attach RIQAS price list reference
$mail.Attachments.Add("C:\Users\ACER\Desktop\claude\hello-world\oas_prices\Randox__RIQAS PRICE LIST 2026 by Jeeranan v2.xlsx")

$mail.Save()
Write-Output "Draft created!"
