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

_อัปเดต 2026-06-21 — เหลือเวลาประมาณ **10 วัน** ก่อนเริ่มงาน_

- [x] ส่งมอบงานที่ Meditop ให้เรียบร้อย — จากกันด้วยดี (วงการนี้แคบ เจอกันอีกแน่)
- [x] เช็คสัญญาจ้างเก่า: มี non-compete clause (ข้อห้ามทำงานคู่แข่ง) หรือไม่
- [ ] อ่าน/ดูข้อมูล cobas pro, cobas pure จากเว็บ Roche Diagnostics
- [ ] ฝึกภาษาอังกฤษโหมดธุรกิจ: self-introduction, account review presentation
- [ ] เตรียม 30-second intro แนะนำตัวกับทีมใหม่ (ไทย + อังกฤษ)
- [ ] พักผ่อน — ช่องว่างระหว่างงานคือโบนัส ใช้ให้คุ้ม

---

## 8. Sprint สุดท้าย 10 วัน (21–30 มิ.ย. 2026)

**เป้าหมาย:** เข้าวันแรกด้วยความมั่นใจ — รู้ portfolio ขั้นต้น + intro พร้อม + ของไม่ค้าง

### ✅ ด้านงาน Meditop (ให้เสร็จก่อน 25 มิ.ย.)
- [x] ส่งไฟล์งาน/รหัสผ่านให้คนรับช่วง
- [x] ลบข้อมูลบริษัทออกจากอุปกรณ์ส่วนตัว (email account, OAS, ไฟล์ราคา)
- [x] ส่ง handover email ถึงหัวหน้า + เพื่อนร่วมงาน

### 📚 ด้านความรู้ Roche (ทำช่วง 21–28 มิ.ย.)
- [ ] **cobas pure** — อ่าน 1 pager: [diagnostics.roche.com](https://diagnostics.roche.com) ค้น "cobas pure"
  - จดจำ: 215+ รายการตรวจ, footprint เล็ก 2 ตร.ม., target แล็บเล็ก-กลาง
- [ ] **cobas pro** — อ่านสไลด์/เว็บ: เรือธง, automation สูง, target รพ.ใหญ่
- [ ] **cobas i 601** — ISE + chemistry + immuno บนแพลตฟอร์มเดียว
- [ ] เปิด LinkedIn ดู profile ของ Account Value Lead / ทีม Roche Thailand ก่อนเจอหน้า

### 🎤 ด้านการสื่อสาร (เตรียมก่อน 28 มิ.ย.)
- [ ] Self-introduction ภาษาอังกฤษ (30 วินาที):
  ```
  "Hi, I'm Job. I've been in lab diagnostics sales for [X] years,
  mostly covering hematology and urinalysis in Bangkok hospitals.
  I'm really excited to join Roche and learn the core lab portfolio —
  especially cobas pure and cobas pro. Looking forward to working with everyone."
  ```
- [ ] ซ้อมออกเสียงจนคล่อง — ไม่ต้องเพอร์เฟกต์ แค่ฟังดูเป็นธรรมชาติ

### 💻 ด้าน Tools ใหม่ (ทำถ้ามีเวลา)
- [ ] ถามทีม Roche ว่าใช้ CRM อะไร (Salesforce? VEEVA?) — เตรียมทำความคุ้นเคย
- [x] เตรียม Notebook/iPad สำหรับจด onboarding — Roche มักมี LMS ของตัวเอง

---

---

## 9. Tools ที่ Roche ใช้จริง — เตรียมก่อนวันแรก

### 🖥️ LMS — Cornerstone OnDemand + cobas Academy
- Roche ใช้ **Cornerstone OnDemand** เป็น platform เรียนรู้หลักทั่วโลก
- มี **cobas Academy cloud** — e-learning เฉพาะสำหรับผลิตภัณฑ์ cobas ทุกรุ่น
- วันแรก HR จะให้ account เข้าระบบ — ดู training history และคอร์สบังคับได้เลย
- เข้าถึงได้ทั้งบน Notebook และ iPad

### 📱 CRM — Veeva Vault CRM (ไม่ใช่ Salesforce แล้ว)
- Roche เลือก **Veeva Vault CRM** — ใช้งานจริงทั่วโลกตั้งแต่ต้นปี 2026
- ออกแบบมาสำหรับ life sciences โดยเฉพาะ (pharma + diagnostics)
- **ใช้หลักบน iPad** — มี offline mode ทำงานได้แม้ไม่มี internet
- สิ่งที่ทำใน Veeva ทุกวัน: บันทึกการเยี่ยมลูกค้า, อัปเดต account, ดู territory plan, แชร์ content ให้ลูกค้า

### 📋 สิ่งที่ต้องเตรียมก่อนวันแรก

| เตรียมอะไร | วิธีทำ | ทำไมสำคัญ |
|---|---|---|
| ทำความรู้จัก Veeva Vault CRM | ดู [Zero to Hero Tutorial](https://intuitionlabs.ai/articles/veeva-vault-crm-zero-to-hero-training-manual-for-pharmaceutical-sales) | วันแรกใช้งานจริงเลย |
| รู้จัก Cornerstone LMS | ค้น YouTube: "Cornerstone OnDemand employee guide" | เปิด onboarding courses ได้ทันที |
| cobas Academy | ขอ account จาก Roche Thailand วันแรก — cobas Academy US ไม่มีเนื้อหาตรง | เรียนผ่าน internal account เท่านั้น |
| เตรียม iPad | ติดตั้ง Veeva CRM app ไว้ล่วงหน้า | ประหยัดเวลาวันแรก |
| ถามทีม IT/HR | Roche ใช้ Vault CRM version ไหน, login ผ่านอะไร | แต่ละ affiliate อาจ config ต่างกัน |

### 🧪 รายการตรวจ (Test Menu) — ภาพรวมที่ต้องรู้

> **หมายเหตุ:** รายชื่อ test ครบถ้วนอยู่ใน eLabDoc (internal system ของ Roche) — ขอ access จาก Application Specialist วันแรก

#### Clinical Chemistry (cobas c 303 / c 503) — 110+ tests
| หมวด | ตัวอย่าง test |
|---|---|
| **Proteins** | Albumin, Total Protein, CRP, Prealbumin |
| **Enzymes** | AST, ALT, ALP, GGT, LDH, Amylase, Lipase |
| **Substrates** | Glucose, Urea (BUN), Creatinine, Uric Acid, Bilirubin (T/D) |
| **Lipids** | Total Cholesterol, Triglycerides, HDL, LDL |
| **Electrolytes** | Ca, Mg, Phosphorus (P), Iron (Fe) |
| **HbA1c** | เบาหวาน — มีบน cobas c 303/503 |
| **DATs** | Drug of abuse screening |
| **TDMs** | ยา vancomycin, digoxin, phenytoin ฯลฯ |

#### Immunoassay ECL (cobas e 402 / e 801) — 100+ tests
| หมวด | ตัวอย่าง test |
|---|---|
| **Thyroid** | TSH, fT3, fT4, Anti-TPO, Anti-TG |
| **Cardiac** | Troponin T Gen.5 (hsTnT), NT-proBNP, CK-MB, Myoglobin |
| **Tumor Markers** | AFP, CEA, CA125, CA19-9, PSA (total/free), CYFRA, NSE, HE4 |
| **Hormones / Fertility** | LH, FSH, Estradiol (E2), Progesterone, Prolactin, hCG, AMH, Inhibin B |
| **Anemia** | Ferritin, Vitamin B12, Folate, EPO |
| **Bone** | PTH, Vitamin D (25-OH), Osteocalcin, β-CrossLaps |
| **Infectious Disease** | HBsAg, Anti-HBs, HCV Ab, HIV Ag/Ab, Syphilis (TPLA) |
| **Inflammation** | Procalcitonin (PCT), IL-6 |
| **Women's Health** | PAPP-A, β-hCG (prenatal screening) |
| **Neurology** | Neurofilament Light (NfL), pTau 181 (Alzheimer's biomarker) |

#### ISE (cobas ISE / ISE Neo) — electrolytes
| test | ความหมาย |
|---|---|
| Na⁺ (Sodium) | ความสมดุลน้ำในร่างกาย |
| K⁺ (Potassium) | หัวใจ, ไต |
| Cl⁻ (Chloride) | acid-base balance |
| Ca²⁺ (iCa) | กระดูก, ต่อมพาราไทรอยด์ (บางรุ่น) |

**specimen ที่รองรับ:** serum, plasma, urine, whole blood, CSF, oral fluid, stool, amniotic fluid

---

## 10. เจาะลึกรายการตรวจแต่ละหมวด (Test Menu Deep Dive)

### 🔬 หมวด A: Clinical Chemistry (cobas c 303 / c 503)

#### A1 — Liver Function Tests (LFT)
| Test | ย่อว่า | ใช้วินิจฉัยอะไร | ค่าปกติโดยรวม |
|---|---|---|---|
| Alanine Aminotransferase | ALT / GPT | ตับอักเสบ, NAFLD, ไวรัสตับอักเสบ — **specific กว่า AST** | ชาย <45, หญิง <35 U/L |
| Aspartate Aminotransferase | AST / GOT | ตับ + กล้ามเนื้อหัวใจ — sensitive กว่าในแอลกอฮอล์ | <40 U/L |
| Alkaline Phosphatase | ALP | ท่อน้ำดีอุดตัน, กระดูก, ตับ | 44–147 U/L |
| Gamma-Glutamyl Transferase | GGT | ดื่มแอลกอฮอล์, ท่อน้ำดี, ยา | ชาย <60, หญิง <40 U/L |
| Total Bilirubin / Direct Bili | T.Bil / D.Bil | ดีซ่าน — แยก pre/intra/post-hepatic | T.Bil <1.2 mg/dL |
| Total Protein / Albumin | TP / ALB | ภาวะโภชนาการ, ตับสร้างโปรตีน | ALB 3.5–5.0 g/dL |

#### A2 — Kidney Function Tests (KFT/RFT)
| Test | ใช้วินิจฉัยอะไร | หมายเหตุ |
|---|---|---|
| Creatinine | ไตเสื่อม, GFR — คำนวณ eGFR ได้ | sensitive น้อยกว่า Cystatin C ในระยะแรก |
| Urea (BUN) | ไตวาย, ภาวะขาดน้ำ | BUN:Creatinine ratio บอก pre/post-renal |
| Uric Acid | เก๊าท์, ไตวายเรื้อรัง | ≥7.0 mg/dL (ชาย) เสี่ยงเก๊าท์ |
| Cystatin C | ตรวจไตระยะแรก — sensitive กว่า creatinine | Roche มี Elecsys Cystatin C |

#### A3 — Lipid Profile
| Test | ใช้วินิจฉัยอะไร |
|---|---|
| Total Cholesterol | คัดกรองโรคหัวใจ |
| Triglycerides (TG) | ไขมันในเลือด, ตับอ่อนอักเสบ |
| HDL-Cholesterol | "ไขมันดี" — ยิ่งสูงยิ่งดี |
| LDL-Cholesterol | "ไขมันเลว" — เป้าหมายในการรักษา |
| Non-HDL Cholesterol | คำนวณได้ — ดีกว่า LDL ในบางกลุ่ม |

#### A4 — Glucose / Diabetes
| Test | ใช้วินิจฉัยอะไร |
|---|---|
| Glucose | เบาหวาน — FBS, RBS, OGTT |
| **HbA1c** | ควบคุมน้ำตาล 3 เดือนย้อนหลัง — **มาตรฐาน monitor DM** |
| Fructosamine | ควบคุมน้ำตาล 2–3 สัปดาห์ — ใช้ใน hemolytic anemia |

#### A5 — Enzymes/Others
| Test | ใช้วินิจฉัยอะไร |
|---|---|
| Amylase / Lipase | ตับอ่อนอักเสบ — Lipase specific กว่า |
| CK (Creatine Kinase) | กล้ามเนื้อ, กล้ามเนื้อหัวใจ, rhabdomyolysis |
| LDH | ทำลายเซลล์ทั่วไป — hemolysis, มะเร็ง |
| Phosphorus / Magnesium | เกลือแร่ — bone, kidney, ICU |
| Iron / TIBC / Transferrin | ธาตุเหล็ก — anemia workup |
| CRP | อักเสบ — infection, autoimmune |
| hsCRP | ความเสี่ยงโรคหัวใจ (Cardiovascular risk) |

---

### 💉 หมวด B: Immunoassay ECL (cobas e 402 / e 801)

#### B1 — Cardiac Markers ⭐ (จุดขายหลักของ Roche)
| Test | ย่อว่า | ใช้วินิจฉัยอะไร | จุดเด่น Roche |
|---|---|---|---|
| **Troponin T Gen 5 (hsTnT)** | hs-cTnT | กล้ามเนื้อหัวใจขาดเลือด (AMI) | **FDA approved** — sensitivity >94%, NPV ≥99% ใน 0+3h protocol |
| NT-proBNP | — | หัวใจล้มเหลว (Heart Failure) — staging และ monitor | ค่าขึ้นลงตาม GFR, ต้องปรับตามอายุ |
| CK-MB | — | AMI เสริม TnT, reperfusion assessment | ลดลงเร็วกว่า TnT → ดูเวลา infarct |
| Myoglobin | — | Early marker AMI — ขึ้นเร็วสุด 2–3 ชม. | sensitivity สูงแต่ specific ต่ำ |

> **Pitch ให้ลูกค้า:** "Troponin T Gen 5 ทำให้ ED rule out AMI ได้ใน 1 ชั่วโมง — ลดเวลา observe ผู้ป่วย ลดต้นทุน รพ."

#### B2 — Thyroid Function
| Test | ใช้วินิจฉัยอะไร | หมายเหตุ |
|---|---|---|
| TSH (3rd/4th gen) | screen ไทรอยด์ผิดปกติ — test แรกที่สั่ง | ค่าปกติ 0.27–4.2 mIU/L |
| fT4 (Free Thyroxine) | hypothyroid / hyperthyroid confirm | ไม่ผันแปรตาม binding protein |
| fT3 (Free Triiodothyronine) | T3 toxicosis, monitor | |
| Anti-TPO | Hashimoto's thyroiditis, Graves' | autoimmune marker |
| Anti-TG | Hashimoto's, thyroid cancer follow-up | |
| Thyroglobulin (Tg) | **follow-up มะเร็งต่อมไทรอยด์** หลังผ่าตัด | ใช้คู่กับ Anti-TG เสมอ |

#### B3 — Tumor Markers
| Test | มะเร็งที่เกี่ยวข้องหลัก | ใช้ทำอะไร |
|---|---|---|
| AFP (Alpha-fetoprotein) | ตับ (HCC), อัณฑะ, รังไข่ | screen + monitor |
| CEA | ลำไส้ใหญ่, ปอด, เต้านม,胃 | monitor การรักษา |
| CA 125 | **มะเร็งรังไข่** | monitor — ไม่แนะนำ screen |
| CA 19-9 | ตับอ่อน, ท่อน้ำดี, ลำไส้ | monitor pancreatic CA |
| CA 15-3 | **เต้านม** | monitor การรักษา |
| PSA (Total/Free) | **ต่อมลูกหมาก** | screen + monitor; Free/Total ratio แยก BPH vs cancer |
| CYFRA 21-1 | ปอด (NSCLC) | monitor, prognosis |
| NSE | ปอด (SCLC), neuroendocrine | monitor |
| HE4 | มะเร็งรังไข่ — specific กว่า CA125 | ใช้คู่ CA125 ใน ROMA score |
| ProGRP | ปอด SCLC | |

> **สำคัญ:** tumor markers ไม่ใช้ diagnose คนเดียว — ใช้ monitor + เสริม imaging

#### B4 — Fertility & Reproductive Hormones
| Test | ใช้ดูอะไร |
|---|---|
| LH / FSH | วงจรรังไข่, วัยทอง, ภาวะมีบุตรยาก |
| Estradiol (E2) | ฟอลลิเคิล, IVF monitoring |
| Progesterone | ตรวจยืนยัน ovulation, ติดตาม IVF |
| Prolactin (PRL) | prolactinoma, ภาวะมีบุตรยาก |
| hCG (total/beta) | ยืนยันตั้งครรภ์, ectopic pregnancy, trophoblastic disease |
| AMH (Anti-Müllerian Hormone) | **Ovarian Reserve** — วางแผน IVF |
| Testosterone (Total/Free) | PCOS (หญิง), hypogonadism (ชาย) |
| SHBG | binding protein — ปรับค่าฮอร์โมน |
| DHEA-S | adrenal function, PCOS |
| Inhibin B | Ovarian reserve เสริม AMH |

#### B5 — Anemia Panel
| Test | ใช้วินิจฉัยอะไร |
|---|---|
| **Ferritin** | Iron store — ต่ำ = iron deficiency, สูง = inflammation/hemochromatosis |
| Vitamin B12 | B12 deficiency anemia, neuropathy |
| Active B12 (Holotranscobalamin) | B12 deficiency ระยะแรก — sensitive กว่า total B12 |
| Folate (Serum/RBC) | Folate deficiency, neural tube defect screening |
| Erythropoietin (EPO) | anemia of chronic disease vs primary |

#### B6 — Bone Markers
| Test | ใช้วินิจฉัยอะไร |
|---|---|
| **Vitamin D (25-OH Total)** | ขาด Vit D — กระดูก, ภูมิคุ้มกัน, DM |
| PTH (Intact) | ต่อมพาราไทรอยด์ — hypercalcemia, CKD-MBD |
| β-CrossLaps (β-CTx) | **bone resorption marker** — monitor ยา anti-resorptive (bisphosphonate) |
| N-MID Osteocalcin | bone formation marker |
| P1NP (Total) | bone formation — WHO standard osteoporosis marker |

#### B7 — Infectious Disease
| Test | วินิจฉัยอะไร |
|---|---|
| HBsAg | ไวรัสตับอักเสบ B — การติดเชื้อปัจจุบัน |
| Anti-HBs | ภูมิคุ้มกัน HBV (วัคซีน/หาย) |
| HBeAg / Anti-HBe | ระยะการติดเชื้อ HBV |
| Anti-HCV | ไวรัสตับอักเสบ C |
| HIV Ag/Ab Combo | HIV — detect ทั้ง p24 antigen + antibody |
| Syphilis (TPLA) | ซิฟิลิส |
| CMV IgG/IgM | CMV — transplant screening |
| Toxoplasma IgG/IgM | ท็อกโซ — หญิงตั้งครรภ์ |
| Rubella IgG/IgM | หัดเยอรมัน — prenatal |

#### B8 — Inflammation & Sepsis
| Test | ใช้วินิจฉัยอะไร | จุดเด่น |
|---|---|---|
| **Procalcitonin (PCT)** | **Sepsis** — แยก bacterial จาก viral/SIRS | ขึ้นเร็ว 3–6 ชม., ใช้ guide antibiotic therapy |
| IL-6 (Interleukin-6) | sepsis early marker — ขึ้นเร็วกว่า PCT | ใช้ใน ICU, COVID-19 severity |
| CRP / hsCRP | อักเสบทั่วไป / cardiovascular risk | |

> **Pitch PCT:** "PCT ช่วยหมอตัดสินใจหยุดยา antibiotic ได้ → ลด antibiotic resistance + ลดค่าใช้จ่าย"

#### B9 — Neurology (ใหม่ล่าสุด)
| Test | ใช้วินิจฉัยอะไร |
|---|---|
| **Neurofilament Light (NfL)** | การบาดเจ็บของเส้นประสาท — MS, ALS, Alzheimer's |
| **pTau 181** | **Alzheimer's disease** biomarker — ใหม่มาก, high medical value |

---

### ⚡ หมวด C: ISE (Ion-Selective Electrode)
| Test | ความหมายทางคลินิก | เชื่อมกับโรคไหน |
|---|---|---|
| Na⁺ (Sodium) | สมดุลน้ำ — hypo/hypernatremia | ไต, ADH, heart failure |
| K⁺ (Potassium) | หัวใจเต้นผิดจังหวะ — hypo/hyperkalemia | ไต, ยา diuretic, DKA |
| Cl⁻ (Chloride) | acid-base balance — metabolic alkalosis/acidosis | |
| Ca²⁺ (Ionized Ca) | ต่อมพาราไทรอยด์, ICU | |

---

### 📊 cobas pure vs cobas pro — จำให้ขึ้นใจ

| หัวข้อ | cobas **pure** | cobas **pro** |
|---|---|---|
| เป้าหมาย | แล็บเล็ก-กลาง | แล็บกลาง-ใหญ่ (รพ.ใหญ่) |
| Footprint | เล็กมาก 2 ตร.ม. | ใหญ่กว่า — modular ต่อขยายได้ |
| Throughput | 120 immuno + 750 mixed/ชม. | สูงสุด **4,400 tests/ชม.** |
| รายการตรวจ | 230+ parameters | 230+ parameters (เมนูกว้างที่สุดใน industry) |
| จุดขายเด่น | ประหยัดพื้นที่, AutoCal ลด calibration 56 ครั้ง/ปี | ความเร็ว, ECL immuno, SonicWash, scalable |
| ISE (เกลือแร่) | มีในตัว | มีในตัว (ISE Neo module ใหม่ 2024) |
| คำถามที่ลูกค้าถามบ่อย | "พื้นที่มีน้อย ใช้ได้ไหม?" → ใช้ได้ 2 ตร.ม. | "throughput ไม่พอ" → ขยาย config ได้ 8 แบบ |

**ข้อมูลสำหรับเล่าให้ลูกค้าฟัง:**
- cobas pure ลด hands-on time ได้ **105 ชั่วโมง/ปี** จาก AutoCal
- cobas pro ลด sample volume ต่อ test ลง **43%** และพลาสติกต่อผล **78%** เทียบรุ่นเก่า
- 93% ของ immunoassay Roche ใช้เวลา **≤ 18 นาที**

### 🤖 AI Features ใน Veeva ที่น่าสนใจ
- **Agentic Call Report** — AI ช่วยเขียนสรุปการเยี่ยมลูกค้าให้อัตโนมัติ
- **Agentic Voice** — บันทึกเสียงแล้ว AI แปลงเป็น call note
- **AI-Powered Media Search** — ค้นหา content ที่อนุมัติแล้วส่งให้ลูกค้าได้ทันที

---

## 11. cobas i 601 — Mass Spectrometry Platform (ใหม่ล่าสุด ธ.ค. 2024)

> **ทำไมสำคัญ:** cobas i 601 คือการปฏิวัติ Core Lab — นำ Mass Spectrometry เข้ามารวมกับ routine analyzer เป็นครั้งแรกในโลก

### เทคโนโลยีที่รวมอยู่ในเครื่องเดียว
| เทคโนโลยี | ทำอะไร |
|---|---|
| **ISE** | Na, K, Cl — electrolytes |
| **Clinical Chemistry** | LFT, KFT, Lipid, Glucose |
| **Immunoassay (ECL)** | Hormone, Cardiac, Tumor Markers |
| **Mass Spectrometry (LC-MS/MS)** | ⭐ ใหม่ — ความแม่นยำสูงสุด, gold standard |

### Mass Spec คืออะไร ทำไม Roche ลงทุนตรงนี้?
- Mass Spectrometry = วิเคราะห์โมเลกุลโดยตรง **ไม่ใช้ antibody** → แม่นกว่า immunoassay มาก
- ปัญหาเดิม: Mass Spec ต้องใช้นักวิทยาศาสตร์เฉพาะทาง, setup ซับซ้อน, ไม่ automated
- cobas i 601 แก้ปัญหานี้: **fully automated, walk-away, integrated กับ core lab**

### รายการตรวจ cobas i 601 (Ionify reagent packs) — เป้าหมาย 60+ analytes
| หมวด | ตัวอย่าง test | ทำไมต้อง Mass Spec |
|---|---|---|
| **Steroid Hormones** | Testosterone (T/F), DHEA-S, Cortisol, Aldosterone, Progesterone | immunoassay มี cross-reactivity — Mass Spec แม่นกว่ามาก |
| **Vitamin D Metabolites** | 25-OH Vit D2, 25-OH Vit D3 (แยกได้) | แยก D2/D3 ได้ชัด vs immunoassay ที่รวมกัน |
| **Immunosuppressants (ISD)** | Tacrolimus, Cyclosporine, Sirolimus, Everolimus | TDM หลัง transplant — ต้องแม่นมาก ชีวิตขึ้นอยู่กับค่านี้ |
| **TDM (Therapeutic Drug Monitoring)** | Vancomycin, antibiotics อื่นๆ | ป้องกัน toxicity + ดื้อยา |
| **Drugs of Abuse (DAT)** | opioids, amphetamines, benzodiazepines | confirm หลัง immunoassay screen |

### สถานะปัจจุบัน (2025–2026)
- **ธ.ค. 2024:** CE Mark approved — launch ใน EU
- **ธ.ค. 2025:** 39 tests approved แล้ว รวม antibiotics TDM
- **เป้าหมาย:** 60+ analytes — rolling out ต่อเนื่อง
- **ไทย:** ยังเป็น emerging market — AVP ที่รู้เรื่องนี้ก่อนจะได้เปรียบมาก

### Pitch ให้ลูกค้า
> *"รพ.ที่ทำ transplant หรือ ICU จะได้ประโยชน์มากที่สุด — TDM immunosuppressants แม่นขึ้น ลด rejection risk และลดค่าใช้จ่ายยาที่ over/under-dose"*

---

## 12. Molecular Diagnostics — cobas PCR Systems (เจาะลึก)

### ทำไม Molecular ถึงสำคัญ
- PCR = ตรวจ DNA/RNA ของเชื้อโดยตรง — **sensitive และ specific สูงสุด** เทียบกับ serology
- ไม่ต้องรอให้ร่างกายสร้าง antibody → จับการติดเชื้อได้ตั้งแต่ระยะแรก
- ใช้ guide การรักษา: ปรับยา, หยุดยา, ติดตาม treatment response

---

### เครื่อง cobas PCR — เรียงตาม throughput
| เครื่อง | Target แล็บ | Throughput/วัน | Walk-away time | อัปเดต |
|---|---|---|---|---|
| **cobas 5800** | แล็บกลาง รพ.ทั่วไป | ~300–400 tests | 4 ชม. | version 2.0 2024 |
| **cobas 6800** | รพ.ใหญ่ ระดับ A/S | สูงสุด **2,112 tests** (dual unit) | **8 ชม.** | version 2.0 ธ.ค. 2024 |
| **cobas 8800** | Reference lab, Blood bank | สูงมาก (batch) | 4 ชม. | version 2.0 ธ.ค. 2024 |

> **cobas 6800/8800 v2.0 (ธ.ค. 2024):** throughput เพิ่ม, sample prioritization, ลด downtime, รวม test menu มากขึ้น

---

### Workflow อัตโนมัติ — จุดขายหลัก
```
Sample in → Sample prep → PCR amplification → Detection → Result + QC → LIS
         (automated)    (automated)          (automated)  (automated)
```
- **walk-away 8 ชั่วโมง** (cobas 6800) — staff ไม่ต้องนั่งเฝ้า
- **Random access** — รัน HIV viral load คู่กับ HPV ในรอบเดียวกันได้
- **Cross-platform standardization** — ค่าจาก 6800 กับ 8800 เทียบกันได้โดยตรง

---

### รายการตรวจ Molecular แยกตามโรค

#### M1 — Viral Hepatitis (สำคัญมากในไทย)
| Test | ใช้ทำอะไร | clinical threshold |
|---|---|---|
| **cobas HBV** (quantitative) | monitor การรักษา HBV | <2,000 IU/mL = inactive; >20,000 = เริ่มยา |
| **cobas HCV** (quantitative) | วัด viral load ก่อน/ระหว่าง DAA therapy | undetectable = sustained virological response (SVR) |
| **cobas MPX** | ตรวจ HIV+HCV+HBV พร้อมกัน | blood donor screening |

> ไทยมีผู้ติดเชื้อ HBV ~6% ของประชากร — ตลาด Molecular Hepatitis ใหญ่มาก

#### M2 — HIV
| Test | ใช้ทำอะไร |
|---|---|
| **cobas HIV-1** (quantitative) | monitor ARV therapy — threshold <200 copies/mL = treatment success |
| HIV-1/HIV-2 qualitative | confirm diagnosis |

> **Clinical rule:** viral load >1,000 copies/mL ระหว่าง ARV → ทำ resistance test → เปลี่ยน regimen

#### M3 — HPV & Cervical Cancer Screening ⭐
| Test | รายละเอียด |
|---|---|
| **cobas HPV** | ตรวจ HR-HPV 14 สายพันธุ์ — รายงาน **16 และ 18 แยก**, pooled 12 สายพันธุ์อื่น |
| HPV 16 | ความเสี่ยงมะเร็งปากมดลูกสูงสุด |
| HPV 18 | ความเสี่ยงสูง รองลงมา |
| HR-HPV อื่น (31,33,35,39,45,51,52,56,58,59,66,68) | รายงานรวม |

**การใช้งาน 3 แบบ:**
1. **Primary HPV screening** — ตรวจ HPV ก่อน Pap smear
2. **Co-testing** — HPV + cytology พร้อมกัน
3. **ASC-US triage** — ใช้ HPV ตัดสินว่าต้องทำ colposcopy ไหม

> **Pitch:** HPV 16 positive → ส่ง colposcopy ทันที แม้ Pap ปกติ — ลด false negative

#### M4 — STI (Sexually Transmitted Infections)
| Test | เชื้อ | specimen |
|---|---|---|
| **cobas CT/NG** | Chlamydia trachomatis + Neisseria gonorrhoeae | urine, swab |
| **cobas TV/MG** | Trichomonas vaginalis + Mycoplasma genitalium | swab |

#### M5 — Tuberculosis
| Test | รายละเอียด |
|---|---|
| **cobas MTB** | ตรวจ Mycobacterium tuberculosis complex (MTBC) — target: 16S rRNA + esx gene |
| **cobas MTB-RIF/INH** | ตรวจดื้อยา **Rifampicin และ Isoniazid** (first-line TB drugs) พร้อมกัน |

> **สำคัญมาก:** Thailand มี TB burden สูง — WHO endorses PCR-based diagnosis แทน culture (รอนาน 6–8 สัปดาห์)

#### M6 — Transplant & Immunocompromised
| Test | ใช้ทำอะไร |
|---|---|
| **CMV DNA** (quantitative) | monitor CMV reactivation หลัง transplant — ปรับยา ganciclovir |
| **EBV DNA** (quantitative) | monitor EBV post-transplant lymphoproliferative disorder (PTLD) |

#### M7 — Blood Donor Screening
| Test | รายละเอียด |
|---|---|
| **cobas MPX** | HIV-1/2 + HCV + HBV — multiplex NAT สำหรับ blood bank |
| **WNV** (West Nile Virus) | บางประเทศ |

#### M8 — cobas omni Utility Channel (LDT)
- แล็บออกแบบ PCR test เองได้บน platform cobas 6800/8800
- validated workflow — ใช้ research assay บน certified instrument
- เหมาะกับ reference lab ที่ต้องการ test พิเศษ

---

### เปรียบเทียบ Molecular vs Serology (Immunoassay)
| หัวข้อ | Molecular (PCR) | Serology (ECL) |
|---|---|---|
| ตรวจอะไร | DNA/RNA ของเชื้อ | Antibody/Antigen ของคน |
| Window period | สั้น — จับได้เร็วกว่า | นาน — ต้องรอ immune response |
| ใช้ monitor | ✅ ดีที่สุด (viral load) | ❌ ไม่เหมาะ |
| ราคา | สูงกว่า | ต่ำกว่า |
| ใช้ screen mass | ❌ แพงเกินไป | ✅ เหมาะ |
| ตัวอย่าง | HBV DNA, HIV viral load | HBsAg, Anti-HCV |

---

---

## 13. Value-Based Selling Framework — คุยกับผู้บริหาร รพ.

### หลักคิดหลัก: "Lab สร้างคุณค่า ไม่ใช่แค่ cost center"
> แล็บใช้งบแค่ **3–4% ของงบ รพ.** แต่ข้อมูลจากแล็บ **ขับเคลื่อน 70% ของการตัดสินใจทางคลินิก**
> นี่คือจุดเริ่มต้นของ pitch ทุกครั้ง

### Framework: Labacoeconomics™ (Roche)
Roche ใช้ concept นี้ในการขาย value ให้ผู้บริหาร รพ. — ไม่ใช่แค่ขายเครื่อง แต่ขาย ROI

| ปัญหาที่ รพ. เจอ | ผลกระทบ | Roche แก้ยังไง |
|---|---|---|
| **Overutilization** — สั่ง test แบบ "shotgun" | 65% ของผลออกมาปกติ — เสียเงินเปล่า, false positive นำไปสู่ cascade ของ test อื่น | Roche ช่วย optimize test menu — สั่งเฉพาะที่ clinical value สูง |
| **Underutilization** — ไม่สั่ง test ที่ควรสั่ง | ผู้ป่วย hyponatremia ที่ mismanage → อยู่ รพ. นานขึ้น **2.6 วัน** — ต้นทุนพุ่ง | High medical value assay (PCT, Troponin T) ช่วยตัดสินใจเร็วขึ้น |
| **Diagnostic variation** — แต่ละหมอสั่ง test ต่างกัน | ต้นทุนผันผวน, คุณภาพการรักษาไม่สม่ำเสมอ | Standardized pathway + data-driven approach |

### สคริปต์ขาย — แบ่งตามคนที่คุย

#### 🏥 ผู้อำนวยการโรงพยาบาล / ฝ่ายการเงิน
> *"แล็บของ รพ. ใช้งบแค่ 3% แต่ข้อมูลที่ได้ขับเคลื่อนการตัดสินใจ 70% ของทีมแพทย์ การลงทุนใน platform ที่ดีกว่า ไม่ใช่ค่าใช้จ่ายเพิ่ม — แต่เป็นการลด length of stay และลด cascade test ที่ไม่จำเป็น"*

**ตัวเลขที่ใช้ได้:**
- PCT ช่วยหยุดยา antibiotic ได้เร็วขึ้น → ลดค่ายา + ลด antibiotic resistance
- Troponin T Gen5 rule out AMI ใน 1 ชม. → ลด observation cost ใน ER
- cobas AutoCal ลด hands-on time **105 ชม./ปี** → staff ทำงานอื่นได้

#### 🔬 หัวหน้าแล็บ / นักเทคนิคการแพทย์
> *"ระบบ automation ลด manual error, walk-away time ยาวขึ้น, calibration อัตโนมัติ — staff ไม่ต้องทำงานซ้ำซากมากขึ้น แต่ throughput ไม่ลด"*

**ตัวเลขที่ใช้ได้:**
- cobas pure: AutoCal ลด calibration event 56 ครั้ง/ปี
- cobas pro: throughput 4,400 tests/ชม.
- cobas 6800: walk-away 8 ชั่วโมง

#### 👨‍⚕️ แพทย์ / KOL
> *"Troponin T Gen5 เป็น FDA-approved hs-cTnT ตัวเดียวในสหรัฐฯ — sensitivity >94% ใน 0+3h protocol ช่วยให้ discharge ผู้ป่วยได้เร็วขึ้นอย่างมั่นใจ"*

### ขั้นตอน Value Selling ในทางปฏิบัติ
1. **ฟังก่อน** — ถามว่า รพ. มีปัญหาอะไร: throughput? accuracy? staff ขาด? cost?
2. **เชื่อมปัญหากับ solution** — อย่านำเสนอเครื่อง นำเสนอผลลัพธ์
3. **ใช้ตัวเลขจริง** — cost per test, hours saved, TAT ที่ลดลง
4. **เสนอ demo / pilot** — ให้แล็บลองใช้จริงก่อนตัดสินใจ
5. **Follow up ด้วย data** — หลัง install วัดผลและรายงานให้ผู้บริหารเห็น ROI

---

## 14. คู่แข่งเจาะลึก — จุดอ่อนที่ Roche ชนะได้

### 🔵 Abbott — Alinity (คู่แข่งตรงสุด)
| หัวข้อ | Abbott Alinity | Roche cobas |
|---|---|---|
| เทคโนโลยี Immuno | CMIA (Chemiluminescent Microparticle) | **ECL (ElectroChemiLuminescence)** |
| จุดอ่อนที่พิสูจน์ได้ | **fT4/fT3 bias ในผู้ป่วย hyperthyroid** — ค่าต่ำกว่าความเป็นจริง non-linearly | Biotin interference (แก้ได้โดยหยุด biotin supplement ก่อนเจาะ) |
| Troponin | TnI (Troponin I) | **TnT Gen5 — FDA approved hs-cTnT** |
| Menu | กว้าง | **กว้างที่สุดใน industry** |

**วิธี counter Abbott:**
> *"ผลการศึกษาพบว่า Alinity ให้ค่า fT4 ต่ำกว่าความเป็นจริงในผู้ป่วย hyperthyroid — อาจทำให้แพทย์ประเมินความรุนแรงต่ำกว่าจริง Roche ECL ไม่มีปัญหานี้"*

---

### 🟡 Siemens Healthineers — Atellica
| หัวข้อ | Siemens Atellica | Roche cobas |
|---|---|---|
| จุดแข็ง Siemens | Automation conveyor ยืดหยุ่น, modular สูง | Throughput สูงกว่า, assay menu กว้างกว่า |
| AMH assay | Positive bias เล็กน้อย | Negative bias เล็กน้อย (ทั้งคู่ต้องพิจารณา ref range) |
| Hepatitis B | ผลดี ใกล้เคียงกัน | **Standard ตลาดไทย** — installed base สูงกว่า |
| Mass Spec | ไม่มี integrated solution | **cobas i 601 — เป็นเจ้าแรกในโลก** |
| Molecular | มี | **cobas 6800/8800 — throughput และ menu กว้างกว่า** |

**วิธี counter Siemens:**
> *"Atellica แข็งเรื่อง automation design แต่ถ้าลูกค้าต้องการ Mass Spec integration หรือ Molecular ที่ครบ Roche เป็นตัวเลือกเดียวที่ทำได้บน platform เดียว"*

---

### 🟠 Beckman Coulter — DxA / AU series
| หัวข้อ | Beckman Coulter | Roche cobas |
|---|---|---|
| จุดแข็ง | ราคาแข่งขันได้ใน chemistry, installed base ใน รพ.เอกชน | Medical value สูงกว่า, support ดีกว่า |
| Troponin | TnI — ไม่ใช่ hs-cTnT | **TnT Gen5 hs — gold standard** |
| Molecular | ไม่มี | **cobas 6800/8800 ครบวงจร** |
| Mass Spec | ไม่มี | **cobas i 601** |
| จุดอ่อน | menu แคบกว่า, innovation ช้ากว่า | |

---

### 🔴 Mindray — BS/CL series
| หัวข้อ | Mindray | Roche cobas |
|---|---|---|
| จุดแข็ง | **ราคาถูกกว่าอย่างชัดเจน** — ชนะในการประมูล รพ.รัฐ tier ล่าง | Medical value, accuracy, support |
| Chemistry accuracy | ค่า bias สูงกว่า Roche อย่างมีนัย (p<0.001) | **แม่นกว่าอย่างมีนัยสำคัญทางสถิติ** |
| Immunoassay | TnI รุ่นใหม่พัฒนาขึ้น แต่ยังห่าง | **ECL + TnT Gen5** |
| Support / Service | พัฒนาขึ้น แต่ยังสู้ Roche ไม่ได้ในไทย | Application Specialist + Service ครบ |
| Molecular | ไม่มี PCR platform เทียบได้ | **cobas 6800/8800** |

**วิธี handle Mindray (เรื่องราคา):**
> *"ถ้าลูกค้าถามว่าทำไมแพงกว่า — ตอบด้วย cost per reportable result ไม่ใช่ราคาเครื่อง: Roche AutoCal ลด calibration เสีย, reagent waste น้อยกว่า, downtime ต่ำกว่า — เมื่อรวมต้นทุนทั้งหมด ส่วนต่างลดลงมาก"*

---

### สรุปตาราง Battlecard
| คู่แข่ง | ใช้เมื่อไหร่ | Roche ชนะด้วยอะไร |
|---|---|---|
| Abbott | ลูกค้าเปรียบ immuno/thyroid | ECL accuracy, TnT Gen5 |
| Siemens | ลูกค้าเน้น automation | Mass Spec, Molecular menu |
| Beckman | ลูกค้า รพ.เอกชน ต้องการ value | Full portfolio, Troponin Gen5 |
| Mindray | ลูกค้าถามราคา | Cost per result, accuracy data, support |

---

---

## 15. Digital Solutions — navify® & cobas infinity

> Roche ไม่ได้ขายแค่เครื่องและ reagent — แต่ขาย **ecosystem ดิจิทัล** ที่เชื่อมทุกอย่างเข้าหากัน

### cobas infinity / navify Lab Operations
| หัวข้อ | รายละเอียด |
|---|---|
| คืออะไร | LIS middleware ของ Roche — เชื่อม analyzer กับ HIS/LIS ของ รพ. |
| ชื่อเดิม | cobas infinity central lab → rebrand เป็น **navify Lab Operations** |
| ทำอะไรได้ | Sample routing อัตโนมัติ, QC monitoring, ส่งผลเข้า LIS เมื่อผ่าน QC เท่านั้น |
| จุดขาย | Browser-based, ไม่ต้องติดตั้ง software เพิ่ม, รองรับ multi-site |

### navify Integrator
- เชื่อมต่อ instrument 100+ ยี่ห้อ (ไม่ใช่แค่ Roche) กับ HIS/LIS/EMR
- Open platform — ลูกค้าที่มีเครื่องยี่ห้ออื่นอยู่แล้วก็ใช้ได้
- **Pitch:** *"แม้ รพ. จะมีเครื่องหลายยี่ห้อ Roche ช่วย integrate ข้อมูลทั้งหมดเข้า LIS ของ รพ. ได้"*

### navify Digital Pathology (uPath Cloud)
- Software สำหรับ pathologist — ดูสไลด์ผ่านจอแทนกล้องจุลทรรศน์
- รวม **AI algorithms 20+** จากพันธมิตร (PathAI, Deep Bio ฯลฯ)
- ตรวจมะเร็ง: prostate, เต้านม, ปอด — AI ช่วยนับ/grade เซลล์
- เชื่อมกับ companion diagnostics (VENTANA) — ใช้ตัดสินใจเลือกยามะเร็ง
- **ความสำคัญสำหรับ AVP:** ทีม pathology คนละทีม แต่รู้ไว้เพื่อเชื่อมโอกาสกับผู้บริหาร

### Roche + AstraZeneca MoU (พ.ค. 2026)
- ขยาย digital pathology + AI ใน **9 ตลาดเอเชีย รวมไทย**
- เป้าหมาย: มะเร็งเต้านม + ปอด — AI วิเคราะห์ผลเพื่อเลือก targeted therapy
- **Pitch ระดับ CEO รพ.:** *"Roche กำลังนำ AI pathology มาไทย — รพ. ที่เตรียมพร้อมจะเป็น center of excellence ด้านมะเร็งในภูมิภาค"*

---

## 16. Territory จริง — รพ. เอกชนไทย ⭐

> Job ดูแล **segment เอกชน** — กระบวนการซื้อแตกต่างจาก รพ. รัฐโดยสิ้นเชิง ตัดสินใจเร็วกว่า ให้ความสำคัญ quality + TAT + service มากกว่าราคา

### กลุ่ม รพ. เอกชนหลักในไทย

#### 🏥 BDMS — Bangkok Dusit Medical Services (ใหญ่ที่สุด)
| รายละเอียด | ข้อมูล |
|---|---|
| จำนวน รพ. | 50+ แห่งทั่วไทย |
| แบรนด์ใน network | Bangkok Hospital, Samitivej, BNH, Phyathai, Paolo, Royal |
| Market share | 20%+ ของตลาด รพ. เอกชนไทย |
| แล็บกลาง | **N Health** — largest blood diagnosis center ในไทย, 80+ สาขา |
| จุดสำคัญ | ตัดสินใจจัดซื้อระดับ group — ชนะที่นี่ได้ = ได้ทั้ง network |

#### 🏥 กลุ่มอื่น ๆ ที่สำคัญ
| กลุ่ม | รพ. หลัก | จุดเด่น |
|---|---|---|
| **Bumrungrad International** | Bumrungrad (สุขุมวิท) | Top 100 โลก (Newsweek 2021–2025), 1.1M patients/ปี, มาตรฐานสูงสุด |
| **Bangkok Chain Hospital** | Vibhavadi, Piyavate | กลาง-เล็ก, กระจายในกรุงเทพ |
| **Praram9 Hospital Group** | Praram9, Praram2 | เน้นลูกค้าประกัน, volume สูง |
| **Vejthani / Petcharavej** | Vejthani, Petcharavej | เน้นต่างชาติ, specialty care |
| **แล็บเอกชนอิสระ** | Synphaet Lab, Doctor Lab | volume สูง, cost per test คือหัวใจ |

---

### คนที่ต้องคุยในการขาย รพ. เอกชน
| บทบาท | ความสำคัญ | สิ่งที่สนใจ |
|---|---|---|
| **หัวหน้าแล็บ / นักเทคนิคการแพทย์** | ⭐⭐⭐ ผู้ใช้จริง | accuracy, ease of use, reagent stability, TAT |
| **แพทย์ (KOL)** | ⭐⭐⭐ มีน้ำหนักในการ approve | clinical value, ผล correlate กับ treatment |
| **ผู้อำนวยการ รพ. / CFO** | ⭐⭐ เซ็นสัญญา | ROI, cost per test, contract terms |
| **จัดซื้อ / Procurement** | ⭐ ดำเนินการ | ราคา, เงื่อนไขสัญญา, after-sales service |

---

### กระบวนการตัดสินใจ รพ. เอกชน (ต่างจาก รพ. รัฐ)
```
ปัญหา/ความต้องการ → หัวหน้าแล็บเปรียบเทียบ → demo/trial
→ แพทย์ KOL ให้ความเห็น → ผู้บริหาร approve → จัดซื้อเจรจาสัญญา
```
- **ไม่มี e-bidding** — ไม่ต้องรอประกาศ ติดต่อได้โดยตรง
- **เร็วกว่า รพ. รัฐ 5–10 เท่า** — บางแห่งตัดสินใจใน 1–3 เดือน
- **สัญญา Reagent Rental** พบบ่อยที่สุด — รพ. ไม่ต้องลงทุนเครื่อง

### ประเภทสัญญาที่พบบ่อย รพ. เอกชน
| ประเภท | ลักษณะ | ระยะ |
|---|---|---|
| **Reagent Rental** ⭐ | ให้เครื่องฟรี เก็บเงินจาก reagent | 3–5 ปี |
| **Cost per reportable** | จ่ายตามผลที่รายงานได้จริง | model ใหม่ — value-based |
| **เช่า** | รพ. จ่ายค่าเช่ารายปี | 3–5 ปี |
| **ซื้อขาด** | รพ. ซื้อเครื่องทันที | น้อยลงเรื่อย ๆ |

### สิ่งที่ รพ. เอกชนให้ความสำคัญมากที่สุด
1. **TAT (Turnaround Time)** — ผลเร็ว = patient experience ดี = ค่าตัวสูงขึ้น
2. **Accuracy & Quality** — accreditation (JCI, HA) ต้องการ QC documentation ที่แน่น
3. **After-sales Service** — downtime = lost revenue — response time ของ Roche สำคัญมาก
4. **Menu กว้าง** — รพ. เดียวทำได้ครบ ไม่ต้อง refer ออก = รายได้ไม่รั่ว
5. **Integration กับ HIS/LIS** — navify integrator คือจุดขายที่ใช้ได้ทันที

---

_แหล่งข้อมูล: Roche Workday job posting (Account Value Partner, Thailand), roche.co.th, diagnostics.roche.com, Thailand Business News (AstraZeneca-Roche MoU), Veeva.com, IntuitionLabs.ai (2026), GlobeNewswire Roche Mass Spec launch Dec 2024, Labacoeconomics™ framework (diagnostics.roche.com), PubMed comparative studies 2024–2025, navify.roche.com, Wikipedia Thailand hospital classification, gprocurement.go.th_
