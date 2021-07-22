<style>
table {
    margin: auto;
}
</style>

# MIMIC-III 數據集介紹

<hr>

## 數據集簡介
* MIMIC-III數據包含**生命體征**、**藥物**、**實驗室量測值**、**醫囑**、**手術編號**、**診斷編號**、**影像報告**、**住院時間**、**生存數據**等。
* 其數據涵蓋2001年至2012年之間進入重症監護病房的成年患者(16歲或以上)的53,426例不同的入院相關數據，以及2001年至2008年收治的7,870名新生兒數據。
  
<br>

* 數據集包含26個數據表，除了字典表之外，標之間透過**患者編號(subject)id**、<strong>病案號(hadm_id)</strong>和<strong>ICU編號(icustay_id)</strong>連接
* 字典表中包含**項目編號(d_item)**、**手術編號(d_icd_procedures)**、<strong>實驗室檢查編號(d_labitems)</strong>等。

## 26張數據表解釋
### 患者基本資訊及院內周轉資訊
| 名稱 | 簡介 | 包含屬性 |
| :-: | :-: | :- |
| ADMISSIONS | 患者入院情況 | 患者編號、病案號、入院時間、出院時間、死亡時間、入院類型、入院地點、出院地點、 |
| CALLOUT | ICU出科即時數據 |  |
| ICUSTAYS | ICU入住數據 |  |
| PATIENTS | 患者數據 |  |
| SERVICES | 患者需要接受的醫療服務 |  |
| TRANSFERS | 患者周轉書據 |  |

<br>

### 患者在ICU期間的各類數據
| 名稱 | 簡介 | 包含屬性 |
| :-: | :-: | :- |
| CAREGIVERS | 護理人員數據 |  |
| CHARTEVENTS | 患者觀察記錄 |  |
| DATETIMEEVENTS | 患者操作時間數據 |  |
| INPUTEVENTS_CV | 使用CV監護系統的入量紀錄 |  |
| INPUTEVENTS_mV | MV系統入量紀錄 |  |
| NOTEEVENTS | 治療紀錄 |  |
| OUTPUTEVENTS | 患者出量紀錄 |  |
| PROCEDUREEVENTS_MV | MV系統操作數據 |  |

<br>

### 醫院紀錄系統收集的各類數據
| 名稱 | 簡介 | 包含屬性 |
| :-: | :-: | :- |
| CPTEVENTS | 患者操作紀錄 |  |
| DIAGNOSES_ICD | 患者診斷ICD9編號 |  |
| DRGCODES | 患者診斷類別 |  |
| LABEVENTS | 患者化驗項目 |  |
| MICROBIOLOGYEVENTS | 病人標本微生物病原體檢測 |  |
| PRESCRIPTIONS | 患者用藥紀錄 |  |
| PROCEDURES_ICD | 患者手術紀錄 |  |

<br>

### 字典資訊
| 名稱 | 簡介 | 包含屬性 |
| :-: | :-: | :- |
| D_CPT | 操作紀錄索引 | CPT code 類別號、類別說明及範圍 |
| D_ICD_DIAGNOSES | 診斷代號索引 | ICD-9 編碼、縮寫、全稱 |
| D_ICD_PROCEDURES | 手術操作代號索引 | ICD-9 編碼、縮寫、全稱 |
| D_ITEMS | 紀錄項目代號索引 | 項目識別碼、項目標籤、標籤縮寫、數據來源 |
| D_LABITEMS | 化驗紀錄代號索引 | 檢測專案識別碼、項目標籤、量測的物質、量測種類 |

