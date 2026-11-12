# -*- coding: utf-8 -*-
"""
Executive 1-Page Resume PDF Generator for Parsa Kodari (پارسا کدری)
Generates a pixel-perfect, 100% justified, RTL-shaped, 1-page executive PDF
with zero letter-reversal bugs and zero font clipping.
"""
import os
import sys
import base64
import subprocess
import shutil

def get_browser_path():
    """Find Google Chrome or Microsoft Edge on the system."""
    candidates = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    # Try PATH
    for name in ['chrome', 'msedge', 'google-chrome', 'chromium']:
        p = shutil.which(name)
        if p:
            return p
    return None

def generate_pdf_via_browser(browser_path, output_pdf='Parsa_Kodari_Resume.pdf'):
    # Load avatar as Base64 WebP / PNG
    avatar_file = 'parsa.png'
    if not os.path.exists(avatar_file):
        avatar_file = 'parsa.webp'
    
    with open(avatar_file, 'rb') as f:
        avatar_b64 = base64.b64encode(f.read()).decode('utf-8')
    mime = 'image/png' if avatar_file.endswith('.png') else 'image/webp'
    avatar_uri = f"data:{mime};base64,{avatar_b64}"

    template_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>رزومه حرفه‌ای پارسا کدری | حسابدار و کارشناس امور مالی</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        @page {{
            size: A4 portrait;
            margin: 10mm 12mm 10mm 12mm;
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        body {{
            font-family: 'Vazirmatn', Tahoma, sans-serif;
            color: #1e2227;
            background: #ffffff;
            direction: rtl;
            font-size: 8.8pt;
            line-height: 1.5;
        }}

        /* Header */
        .resume-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 8px;
            border-bottom: 2.5px solid #87142b;
            margin-bottom: 8px;
        }}

        .header-avatar {{
            width: 72px;
            height: 90px;
            border-radius: 8px;
            object-fit: cover;
            border: 2px solid #87142b;
            flex-shrink: 0;
            box-shadow: 0 2px 6px rgba(135, 20, 43, 0.15);
        }}

        .header-info {{
            flex: 1;
            padding: 0 18px;
        }}

        .header-info h1 {{
            font-size: 19pt;
            font-weight: 800;
            color: #87142b;
            line-height: 1.2;
            margin-bottom: 2px;
            letter-spacing: -0.3px;
        }}

        .header-info h2 {{
            font-size: 10.5pt;
            font-weight: 700;
            color: #1e2227;
            margin-bottom: 3px;
        }}

        .header-info p.sub1 {{
            font-size: 8.4pt;
            color: #87142b;
            font-weight: 600;
            margin-bottom: 2px;
        }}

        .header-info p.sub2 {{
            font-size: 7.8pt;
            color: #5a6370;
            font-weight: 500;
        }}

        .header-contact {{
            font-size: 8pt;
            color: #3a414b;
            line-height: 1.6;
            flex-shrink: 0;
            text-align: right;
            direction: rtl;
        }}

        .c-item {{
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 6px;
        }}

        .c-lbl {{
            font-weight: 700;
            color: #87142b;
            min-width: 62px;
        }}

        .c-val {{
            color: #22262b;
            font-weight: 500;
        }}

        .c-val.ltr {{
            direction: ltr;
            unicode-bidi: embed;
            font-family: 'Vazirmatn', -apple-system, sans-serif;
        }}

        /* Section Headings */
        .sec-title {{
            background: #87142b;
            color: #ffffff;
            font-size: 9.5pt;
            font-weight: 700;
            padding: 3.5px 10px;
            border-radius: 3px;
            margin-top: 8px;
            margin-bottom: 5px;
            letter-spacing: -0.2px;
        }}

        /* Summary (Justified) */
        .summary-box {{
            font-size: 8.5pt;
            line-height: 1.65;
            text-align: justify;
            text-justify: inter-word;
            color: #24292f;
            padding: 2px 2px;
        }}

        /* Jobs */
        .job-item {{
            margin-bottom: 7px;
        }}

        .job-row {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 2px;
        }}

        .job-title-company {{
            font-size: 9pt;
        }}

        .job-role {{
            font-weight: 700;
            color: #87142b;
        }}

        .job-sep {{
            color: #87142b;
            margin: 0 4px;
            font-weight: 700;
        }}

        .job-company {{
            font-weight: 600;
            color: #1e2227;
        }}

        .job-url {{
            font-size: 7.6pt;
            color: #5a6370;
            direction: ltr;
            unicode-bidi: embed;
            display: inline-block;
            white-space: nowrap;
        }}

        .job-date {{
            font-size: 7.8pt;
            color: #5a6370;
            font-weight: 600;
            white-space: nowrap;
            direction: rtl;
            background: #f4f6f8;
            padding: 1px 8px;
            border-radius: 3px;
        }}

        .job-tasks {{
            list-style: none;
            padding-right: 14px;
        }}

        .job-tasks li {{
            position: relative;
            font-size: 8pt;
            line-height: 1.5;
            color: #333942;
            margin-bottom: 1.5px;
            text-align: justify;
            text-justify: inter-word;
        }}

        .job-tasks li::before {{
            content: "•";
            position: absolute;
            right: -12px;
            color: #87142b;
            font-weight: 700;
            font-size: 9pt;
        }}

        /* Education & Skills Rows */
        .edu-item {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 4px;
            font-size: 8.4pt;
        }}

        .edu-main {{
            color: #24292f;
        }}

        .edu-main b {{
            color: #1e2227;
            font-weight: 700;
        }}

        .edu-status {{
            font-size: 7.6pt;
            color: #5a6370;
            font-weight: 600;
            white-space: nowrap;
            direction: rtl;
            background: #f4f6f8;
            padding: 1px 8px;
            border-radius: 3px;
        }}

        .skill-line {{
            font-size: 8.2pt;
            line-height: 1.6;
            color: #24292f;
            margin-bottom: 3px;
            text-align: justify;
            text-justify: inter-word;
        }}

        .skill-line b {{
            color: #87142b;
            font-weight: 700;
        }}

        /* Subtle Footer */
        .resume-footer {{
            margin-top: 10px;
            padding-top: 5px;
            border-top: 1px solid #e5e8ec;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 7.2pt;
            color: #8c95a1;
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <div class="resume-header">
        <img src="{avatar_uri}" alt="پارسا کدری" class="header-avatar">
        <div class="header-info">
            <h1>پارسا کدری</h1>
            <h2>حسابدار و کارشناس امور مالی | متولد ۱۳۸۵ (۲۰۰۶)</h2>
            <p class="sub1">دانشجوی کارشناسی حسابداری دانشگاه آزاد اسلامی واحد تهران مرکزی (سوهانک)</p>
            <p class="sub2">دارای مدرک حسابداری جامع و گواهینامه سپیدار سیستم از مجتمع فنی تهران</p>
        </div>
        <div class="header-contact">
            <div class="c-item"><span class="c-lbl">ایمیل:</span><span class="c-val ltr">Parsa.kodari@gmail.com</span></div>
            <div class="c-item"><span class="c-lbl">تلفن:</span><span class="c-val ltr">0903 444 3342</span></div>
            <div class="c-item"><span class="c-lbl">اینستاگرام:</span><span class="c-val ltr">@Parsa___kodari</span></div>
            <div class="c-item"><span class="c-lbl">محل سکونت:</span><span class="c-val">تهران، سعادت‌آباد</span></div>
            <div class="c-item"><span class="c-lbl">وب‌سایت:</span><span class="c-val ltr">parsakodari.ir</span></div>
        </div>
    </div>

    <!-- خلاصه حرفه‌ای -->
    <div class="sec-title">خلاصه حرفه‌ای و اهداف کاری</div>
    <div class="summary-box">
        دانشجوی کارشناسی حسابداری دانشگاه آزاد اسلامی تهران مرکزی و دانش‌آموخته دوره جامع حسابداری و سپیدار سیستم از مجتمع فنی تهران (MFT). برخوردار از تجارب عملی در حسابداری فروشگاهی، انبارداری و کنترل موجودی کالا (فروشگاه‌های آنلاین رویال دیجی و دی‌پی کامپیوتر)، حسابداری شرکت‌های گردشگری و همایشی، مدیریت و تسویه تنخواه‌گردان، ثبت دریافت‌ها و پرداخت‌ها و مغایرت‌گیری بانکی. فردی دقیق، منظم، با انضباط مالی بالا و علاقه‌مند به کار تیمی و توسعه راهکارهای نوین مالی.
    </div>

    <!-- سوابق شغلی -->
    <div class="sec-title">سوابق شغلی و تجارب اجرایی</div>

    <div class="job-item">
        <div class="job-row">
            <div class="job-title-company">
                <span class="job-role">حسابدار مالی</span>
                <span class="job-sep">|</span>
                <span class="job-company">شرکت زمان‌نما پویش مهراد</span>
            </div>
            <div class="job-date">شهریور ۱۴۰۵ — آبان ۱۴۰۵</div>
        </div>
        <ul class="job-tasks">
            <li>ثبت و رسیدگی روزانه به اسناد مالی، کنترل صحت فاکتورها و بایگانی دفاتر مالی</li>
            <li>انجام مغایرت‌گیری بانکی دوره‌ای و کنترل حساب‌های تجاری طرف‌های حساب</li>
            <li>نظارت، مدیریت و تسویه هزینه‌ها و حساب‌های تنخواه‌گردان مجموعه</li>
        </ul>
    </div>

    <div class="job-item">
        <div class="job-row">
            <div class="job-title-company">
                <span class="job-role">حسابدار و مسئول کنترل موجودی و انبارداری</span>
                <span class="job-sep">|</span>
                <span class="job-company">فروشگاه‌های آنلاین رویال دیجی و دی‌پی کامپیوتر</span>
                <span class="job-url">(royaldigi.ir / dpcomputer.ir)</span>
            </div>
            <div class="job-date">تیر ۱۴۰۵ — شهریور ۱۴۰۵</div>
        </div>
        <ul class="job-tasks">
            <li>حسابداری فروشگاهی، صدور فاکتور و تطبیق تسویه‌حساب درگاه‌های پرداخت آنلاین</li>
            <li>انبارگردانی ادواری، کنترل کاردکس کالا، بررسی مغایرت‌ها و کسری/اضافات انبار کالای دیجیتال</li>
            <li>ثبت اسناد دریافت و پرداخت طرف‌های تجاری و تأمین‌کنندگان قطعات کامپیوتر</li>
        </ul>
    </div>

    <div class="job-item">
        <div class="job-row">
            <div class="job-title-company">
                <span class="job-role">حسابدار</span>
                <span class="job-sep">|</span>
                <span class="job-company">شرکت خدمات مسافرتی و گردشگری سرزمین اساطیری</span>
            </div>
            <div class="job-date">مرداد ۱۴۰۴ — آبان ۱۴۰۴</div>
        </div>
        <ul class="job-tasks">
            <li>ثبت اسناد مالی مربوط به تورها، اقامتگاه‌ها و تسویه‌حساب با آژانس‌های همکار</li>
            <li>مدیریت تنخواه هزینه‌های عملیاتی تورها و بررسی اسناد مثبته هزینه‌ای</li>
        </ul>
    </div>

    <div class="job-item">
        <div class="job-row">
            <div class="job-title-company">
                <span class="job-role">ادمین و هماهنگ‌کننده اجرایی</span>
                <span class="job-sep">|</span>
                <span class="job-company">شرکت همایشگران سام</span>
            </div>
            <div class="job-date">اردیبهشت ۱۴۰۴ — آذر ۱۴۰۴</div>
        </div>
        <ul class="job-tasks">
            <li>هماهنگی امور اداری و اجرایی برگزاری سمینارها و همایش‌ها و پاسخگویی به مراجعین</li>
            <li>مستندسازی رویدادها، آرشیو دیجیتال اسناد و پیگیری قراردادهای کارفرمایان</li>
        </ul>
    </div>

    <div class="job-item">
        <div class="job-row">
            <div class="job-title-company">
                <span class="job-role">کمک‌حسابدار و مسئول تنخواه‌گردان</span>
                <span class="job-sep">|</span>
                <span class="job-company">مجموعه آموزشی و مهدکودک ققنوس</span>
            </div>
            <div class="job-date">خرداد ۱۴۰۴ — آذر ۱۴۰۴</div>
        </div>
        <ul class="job-tasks">
            <li>ثبت و کنترل روزانه دریافت‌ها (شهریه) و پرداخت‌های جاری و هزینه‌های عملیاتی</li>
            <li>مدیریت کامل تنخواه‌گردان و ساماندهی فاکتورها و انجام مغایرت‌گیری بانکی</li>
        </ul>
    </div>

    <div class="job-item">
        <div class="job-row">
            <div class="job-title-company">
                <span class="job-role">ادمین و مسئول امور اداری</span>
                <span class="job-sep">|</span>
                <span class="job-company">انجمن صنفی آشپزان و سرآشپزان ایران</span>
            </div>
            <div class="job-date">خرداد ۱۴۰۳ — دی ۱۴۰۳</div>
        </div>
        <ul class="job-tasks">
            <li>مدیریت دبیرخانه، تنظیم صورتجلسات و مکاتبات اداری، ساماندهی پرونده‌های اعضا</li>
        </ul>
    </div>

    <!-- تحصیلات -->
    <div class="sec-title">تحصیلات و دوره‌های تخصصی</div>

    <div class="edu-item">
        <div class="edu-main"><b>کارشناسی حسابداری</b> — دانشگاه آزاد اسلامی، واحد تهران مرکزی (مجتمع سوهانک)</div>
        <div class="edu-status">در حال تحصیل (کارشناسی)</div>
    </div>
    <div class="edu-item">
        <div class="edu-main"><b>دوره جامع حسابداری و نرم‌افزار سپیدار</b> — مجتمع فنی تهران (MFT)</div>
        <div class="edu-status">گواهینامه رسمی</div>
    </div>
    <div class="edu-item">
        <div class="edu-main"><b>گواهینامه تخصصی ICDL (اکسل مالی، ویندوز و آفیس)</b></div>
        <div class="edu-status">مهارت‌های هفتگانه</div>
    </div>

    <!-- مهارت‌ها -->
    <div class="sec-title">مهارت‌های تخصصی، نرم‌افزارها و زبان خارجی</div>
    <div class="skill-line"><b>نرم‌افزارهای حسابداری:</b> سپیدار سیستم همکاران سیستم (پیشرفته) | نرم‌افزار هلو (مسلط) | شایگان سیستم (مسلط)</div>
    <div class="skill-line"><b>مهارت‌های مالی و اداری:</b> اکسل مالی و فرمول‌نویسی تخصصی | مغایرت‌گیری بانکی | مدیریت تنخواه‌گردان | انبارداری و کنترل کاردکس کالا</div>
    <div class="skill-line"><b>زبان خارجی و عمومی:</b> زبان انگلیسی (متوسط رو به بالا - مسلط به اصطلاحات حسابداری و مالی) | سرعت عمل و دقت بالا در محاسبات</div>

    <!-- Footer -->
    <div class="resume-footer">
        <span>رزومه رسمی پارسا کدری — حسابدار و کارشناس امور مالی</span>
        <span>parsakodari.ir | 0903 444 3342</span>
    </div>

</body>
</html>'''

    temp_html = os.path.abspath('resume_print_template.html')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(template_html)

    out_abs = os.path.abspath(output_pdf)
    cmd = [
        browser_path,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={out_abs}',
        temp_html
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    print(f"[OK] Generated {output_pdf} successfully via {os.path.basename(browser_path)}!")

if __name__ == '__main__':
    browser = get_browser_path()
    if browser:
        generate_pdf_via_browser(browser, 'Parsa_Kodari_Resume.pdf')
        if os.path.exists('Data'):
            shutil.copy('Parsa_Kodari_Resume.pdf', 'Data/Parsa_Kodari_Resume.pdf')
            print("[OK] Copied to Data/Parsa_Kodari_Resume.pdf")
    else:
        print("[ERROR] Chrome or Edge not found on system!")
        sys.exit(1)
