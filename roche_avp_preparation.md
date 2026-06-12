# เตรียมตัวสู่ Roche Diagnostics — Account Value Partner (AVP)

_สร้างเมื่อ: 2026-06-12 | เริ่มงาน: กรกฎาคม 2026_

---

## 1. ตำแหน่งนี้ทำอะไร (จาก Job Posting ของ Roche Thailand)

**Account Value Partner** = เซลส์ภาคสนามที่เน้น "ขายคุณค่า" (value-based selling) ไม่ใช่แค่ขายเครื่อง

| หน้าที่หลัก | ความหมายในทางปฏิบัติ |
|---|---|
| ทำยอดขายตามเป้า + คุมต้นทุน | เหมือนเดิมจาก Meditop แต่ scale ใหญ่ขึ้น |
| Territory & Account Planning | วางแผนรายพื้นที่/รายโรงพยาบาล สอดคล้องกับแผนการตลาด |
| KOL Engagement Strategy | สร้างความสัมพันธ์กับอาจารย์แพทย์/นักเทคนิคการแพทย์ผู้นำความคิด |
| Medical Education Events | จัดงานวิชาการ/อบรมให้ลูกค้า — **ทักษะใหม่ที่ต้องฝึก** |
| Co-create solutions กับผู้บริหาร รพ. | คุยระดับ ผอ.รพ. / หัวหน้าแล็บ ไม่ใช่แค่จัดซื้อ |
| ดูแล full sales cycle | ตั้งแต่หาลูกค้า → ปิดสัญญา → ประสานงานหลังการขาย |

**รายงานตรงต่อ:** Account Value Lead (ทีม Sales)
**คุณสมบัติที่ Roche ต้องการ:** จบเทคนิคการแพทย์, ประสบการณ์ขาย 3+ ปี, ไทย+อังกฤษดี, เดินทางต่างจังหวัดได้

---

## 2. รู้จัก Roche Diagnostics Thailand

- ก่อตั้งในไทยปี 1999 พนักงาน 300+ คน — เป็นเบอร์ 1 ตลาด IVD โลก
- ข่าวสำคัญ พ.ค. 2026: **Roche + AstraZeneca เซ็น MoU 3 ปี** ผลักดัน AI digital pathology ใน 9 ตลาดเอเชียรวมไทย (มะเร็งเต้านม/ปอด) → หัวข้อคุยกับลูกค้าได้
- จุดขายหลักของ Roche: ระบบอัตโนมัติครบวงจร + เมนูตรวจกว้าง + medical value สูง

## 3. Portfolio ที่ต้องเรียนรู้ก่อนเริ่มงาน (เรียงตามความสำคัญ)

| ลำดับ | ระบบ | ใช้กับแล็บแบบไหน |
|---|---|---|
| 1 | **cobas pro integrated solutions** | แล็บปริมาณกลาง-สูง (รพ.ใหญ่) — เรือธงปัจจุบัน |
| 2 | **cobas pure integrated solutions** | แล็บเล็ก-กลาง, พื้นที่จำกัด 2 ตร.ม., 215+ รายการตรวจ |
| 3 | **cobas i 601 / Mass Spec** | เทคโนโลยีใหม่ — รวม ISE + chemistry + immuno + mass spec บนแพลตฟอร์มเดียว |
| 4 | Molecular (PCR), Point of Care | เสริมภาพรวม portfolio |

**ข้อได้เปรียบของ Job:** เคยขาย Roche cobas สมัย Meditop อยู่แล้ว → ไม่ได้เริ่มจากศูนย์

## 4. แผนที่คู่แข่งในตลาด Core Lab ไทย

| คู่แข่ง | แพลตฟอร์มหลัก | จุดที่ต้องระวัง |
|---|---|---|
| Abbott | Alinity | คู่แข่งตรงสุดใน immunoassay |
| Siemens Healthineers | Atellica | แข็งเรื่อง automation |
| Beckman Coulter | DxA series | ราคาแข่งขันได้ |
| Mindray | BS/CL series | ตีตลาดด้วยราคา โดยเฉพาะ รพ.รัฐ |
| Sysmex | (hematology/urinalysis) | อดีตสินค้าที่เราขาย — ตอนนี้คนละ segment แต่เจอกันในแล็บเดียวกัน |

**ข้อได้เปรียบ:** Job รู้กระบวนการจัดซื้อ รพ.รัฐ, สเปคล็อค, OAS/e-bidding จากฝั่ง Meditop ดีมาก

## 5. ⚠️ ข้อมูลเก่าจาก Meditop — ใช้อะไรได้/ไม่ได้

| ใช้ได้ (ติดตัวไป) | ห้ามใช้ (ความลับบริษัทเก่า) |
|---|---|
| ทักษะการขาย, ความสัมพันธ์ส่วนตัว | ❌ ราคาในสัญญา (contract_conditions.json) |
| ความรู้ workflow แล็บ, cost-per-test | ❌ Price list ภายใน (oas_prices/) |
| ความเข้าใจกระบวนการจัดซื้อ รพ. | ❌ ประวัติใบเสนอราคา (quotation_history.json) |
| Framework/template ที่สร้างเอง | ❌ ข้อมูลลูกค้าเชิงพาณิชย์ของ Meditop |

> การเอาข้อมูลราคา/สัญญาของนายจ้างเก่าไปใช้ที่ใหม่ = ผิดจรรยาบรรณและอาจผิดกฎหมาย (PDPA/trade secret) — สิ่งที่ Roche จ้างเราคือ "ทักษะ" ไม่ใช่ "ไฟล์"

## 6. แผน 30-60-90 วัน (ก.ค.–ก.ย. 2026)

**วันที่ 1–30: เรียนรู้**
- เข้า onboarding/training ของ Roche ให้เต็มที่ — จดทุกอย่างเป็นระบบ
- เรียน portfolio: cobas pro/pure ให้คล่อง (spec, จุดขาย, คำถามที่ลูกค้าถามบ่อย)
- ทำความรู้จักทีม: Account Value Lead, Application Specialist, Service, Marketing
- ขอ account list + ประวัติยอดขายของ territory ที่รับผิดชอบ

**วันที่ 31–60: ลงสนาม**
- เยี่ยมลูกค้าทุกรายใน territory อย่างน้อย 1 รอบ (แนะนำตัว + ฟังปัญหา)
- ระบุ KOL หลักในพื้นที่ + เริ่มสร้างความสัมพันธ์
- ร่าง territory plan ฉบับแรก ส่งให้หัวหน้าดู

**วันที่ 61–90: สร้างผลงาน**
- ปิด quick win อย่างน้อย 1 ดีล (reagent/menu expansion ง่ายกว่าเครื่องใหม่)
- เสนอจัด medical education event เล็กๆ 1 งาน
- Review territory plan กับ Account Value Lead

## 7. เตรียมตัวเดือนนี้ (มิ.ย. ก่อนเริ่มงาน)

- [ ] ส่งมอบงานที่ Meditop ให้เรียบร้อย — จากกันด้วยดี (วงการนี้แคบ เจอกันอีกแน่)
- [ ] เช็คสัญญาจ้างเก่า: มี non-compete clause (ข้อห้ามทำงานคู่แข่ง) หรือไม่
- [ ] อ่าน/ดูข้อมูล cobas pro, cobas pure จากเว็บ Roche Diagnostics
- [ ] ฝึกภาษาอังกฤษโหมดธุรกิจ: self-introduction, account review presentation
- [ ] เตรียม 30-second intro แนะนำตัวกับทีมใหม่ (ไทย + อังกฤษ)
- [ ] พักผ่อน — ช่องว่างระหว่างงานคือโบนัส ใช้ให้คุ้ม

---

_แหล่งข้อมูล: Roche Workday job posting (Account Value Partner, Thailand), roche.co.th, diagnostics.roche.com, Thailand Business News (AstraZeneca-Roche MoU)_
