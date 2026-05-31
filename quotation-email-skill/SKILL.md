---
name: quotation-email
description: >
  ใช้สกิลนี้ทุกครั้งที่ Job ต้องการเขียนอีเมลเสนอราคา (quotation email) ส่งลูกค้าโรงพยาบาล
  สกิลนี้ช่วยสร้างอีเมลภาษาไทย Formal สำหรับสินค้า Medical Device / Laboratory Diagnostics
  โดยเฉพาะ Sysmex UA/UF Series, Sysmex CBC XN-3000, Dirui Analyzers, Sciendox Feces Analyzer
  Trigger เมื่อ: "เขียนอีเมลเสนอราคา", "ส่งใบเสนอราคา", "draft email quotation",
  "เขียนอีเมลให้ลูกค้า", "ส่งราคาให้", "email ราคา", "เสนอราคา" หรือบริบทที่ต้องสร้างอีเมลขายสินค้า medical
---

# Quotation Email Skill — สำหรับ Job (Meditop)

## บริบท
- ผู้ใช้: Job — Sales Representative, Meditop Co., Ltd.
- อุตสาหกรรม: Medical devices / Laboratory diagnostics
- ลูกค้า: โรงพยาบาลในกรุงเทพฯ
- ภาษาหลัก: **ภาษาไทย (Formal)**
- Tone: สุภาพ เป็นทางการ มืออาชีพ — ไม่ oversell

---

## ขั้นตอนการ Generate อีเมล

### Step 1: รับข้อมูลจาก Job
ถามหรือรับข้อมูลต่อไปนี้ก่อน generate (ถ้ายังไม่ครบ):

| ข้อมูล | จำเป็น | ตัวอย่าง |
|---|---|---|
| ชื่อโรงพยาบาล | ✅ | โรงพยาบาลรามาธิบดี |
| ชื่อผู้รับ + ตำแหน่ง | ✅ | คุณสิริพร / หัวหน้าแล็บ |
| Product line | ✅ | Sysmex UF-4000 |
| ราคา | ✅ | 1,250,000 บาท |
| เงื่อนไขพิเศษ | ⬜ | ฟรีติดตั้ง + อบรม 2 วัน |
| จุดขายที่อยากเน้น | ⬜ | Workflow speed, cost-per-test |
| ประเภทผู้รับ | ✅ | แพทย์/หัวหน้าแล็บ หรือ จัดซื้อ |
| Structure | ✅ | สั้นกระชับ / ละเอียด / ยืดหยุ่น |
| Context พิเศษ | ⬜ | เคยนัดพบแล้ว / ส่งตามที่คุยไว้ |

### Step 2: เลือก Template ตาม Product Line
อ่านไฟล์ reference ที่ตรงกับสินค้า:
- Sysmex UA/UF Series → `references/sysmex-ua-uf.md`
- Sysmex CBC XN-3000 → `references/sysmex-xn3000.md`
- Dirui Analyzers → `references/dirui.md`
- Sciendox Feces Analyzer → `references/sciendox.md`

### Step 3: ปรับ Tone ตามผู้รับ
- **แพทย์ / หัวหน้าแล็บ**: เน้น clinical benefit, workflow, คุณภาพผล — ใช้ภาษาวิชาการเล็กน้อย
- **จัดซื้อโรงพยาบาล**: เน้นราคา, เงื่อนไข, การรับประกัน, บริการหลังการขาย — ใช้ภาษาธุรกิจ

### Step 4: เลือก Structure
- **สั้นกระชับ**: 3-4 ย่อหน้า ไม่มี bullet — เหมาะส่งตาม email ทั่วไป
- **ละเอียด + bullet points**: มี section จุดเด่นสินค้า — เหมาะเมื่อต้องการ impress
- **ยืดหยุ่น**: ให้ Job เลือกตอน generate

---

## โครงสร้างอีเมลมาตรฐาน

```
Subject: [ชัดเจน ระบุสินค้าและโรงพยาบาล]

เรียน [ชื่อ-นามสกุล / ตำแหน่ง],

[Opening: อ้างอิงการพบกัน หรือ intro บริษัท]

[Body: นำเสนอสินค้า + จุดเด่น 2-3 ข้อ]

[Pricing section: ราคา + เงื่อนไข]

[Closing: CTA ชัดเจน + เปิดทางติดต่อ]

ขอแสดงความนับถือ,
Job [นามสกุล]
Sales Representative | Meditop Co., Ltd.
โทร: [เบอร์] | อีเมล: [อีเมล]
```

---

## ตัวแปร Follow-up / Variants

หลัง generate อีเมลหลักแล้ว ให้เสนอ variants เพิ่ม:
- 🔁 **Follow-up**: กรณีลูกค้ายังไม่ตอบใน 3-5 วัน
- 📎 **With attachment**: เมื่อแนบ PDF quotation ด้วย
- 🏥 **Tender version**: ภาษาทางการสำหรับระบบจัดซื้อ/ประมูล
- 🤝 **Post-meeting**: ส่งหลังนัดพบ อ้างอิงสิ่งที่คุยกัน

---

## สิ่งที่ต้องหลีกเลี่ยง
- ❌ ภาษาที่ oversell หรือ pushy เกินไป
- ❌ ประโยคยาวซับซ้อน
- ❌ ใช้ศัพท์เทคนิคมากเกินไปกับจัดซื้อ
- ❌ ลืม CTA (call to action) ท้ายอีเมล
- ❌ Subject line คลุมเครือ
