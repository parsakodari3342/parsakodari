import os
import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Tahoma fonts
pdfmetrics.registerFont(TTFont('Tahoma', r'C:\Windows\Fonts\tahoma.ttf'))
pdfmetrics.registerFont(TTFont('Tahoma-Bold', r'C:\Windows\Fonts\tahomabd.ttf'))

def fa(text):
    if not text:
        return ""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

def generate_executive_resume(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=26,
        bottomMargin=26
    )

    story = []

    # Palette
    crimson = colors.HexColor('#87142b')
    crimson_light = colors.HexColor('#a81c38')
    crimson_bg = colors.HexColor('#fcf2f4')
    charcoal = colors.HexColor('#1e2227')
    gray_dark = colors.HexColor('#3a414b')
    gray_muted = colors.HexColor('#5a6370')
    line_color = colors.HexColor('#e2e6eb')

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Tahoma-Bold',
        fontSize=18,
        leading=24,
        textColor=crimson,
        alignment=2 # Right
    )

    contact_style = ParagraphStyle(
        'ContactText',
        fontName='Tahoma',
        fontSize=8,
        leading=12.5,
        textColor=gray_dark,
        alignment=2
    )

    sec_title_style = ParagraphStyle(
        'SectionTitle',
        fontName='Tahoma-Bold',
        fontSize=10,
        leading=13.5,
        textColor=colors.white,
        alignment=2
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        fontName='Tahoma-Bold',
        fontSize=9,
        leading=12,
        textColor=crimson,
        alignment=2
    )

    item_date_style = ParagraphStyle(
        'ItemDate',
        fontName='Tahoma',
        fontSize=7.5,
        leading=10.5,
        textColor=gray_muted,
        alignment=0 # Left
    )

    body_style = ParagraphStyle(
        'Body',
        fontName='Tahoma',
        fontSize=8,
        leading=12,
        textColor=charcoal,
        alignment=2
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        fontName='Tahoma',
        fontSize=7.8,
        leading=11,
        textColor=charcoal,
        alignment=2
    )

    # 1. Header (Photo + Title + Contact Info)
    photo_w = 64
    photo_h = 80
    avatar = Image('parsa.png', width=photo_w, height=photo_h)

    header_data = [
        [
            Paragraph(
                f"<b>{fa('ایمیل:')}</b> Parsa.kodari@gmail.com<br/>"
                f"<b>{fa('تلفن:')}</b> 0903 444 3342<br/>"
                f"<b>{fa('اینستاگرام:')}</b> @Parsa___kodari<br/>"
                f"<b>{fa('محل سکونت:')}</b> {fa('تهران، سعادت‌آباد')}<br/>"
                f"<b>{fa('وب‌سایت:')}</b> parsakodari.ir",
                contact_style
            ),
            Paragraph(
                f"{fa('پارسا کدری')}<br/>"
                f"<font size='10' color='#1e2227'><b>{fa('حسابدار و کارشناس امور مالی | متولد ۲۰۰۶')}</b></font><br/>"
                f"<font size='8' color='#87142b'>{fa('دانشجوی کارشناسی حسابداری دانشگاه آزاد اسلامی واحد تهران مرکزی (سوهانک)')}</font><br/>"
                f"<font size='7.5' color='#5a6370'>{fa('دارای مدرک حسابداری جامع و گواهینامه سپیدار سیستم از مجتمع فنی تهران')}</font>",
                title_style
            ),
            avatar
        ]
    ]

    header_table = Table(header_data, colWidths=[180, 285, 70])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (2,0), (2,0), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=crimson, spaceAfter=6, spaceBefore=4))

    def make_sec_header(title_text):
        p = Paragraph(fa(title_text), sec_title_style)
        t = Table([[p]], colWidths=[535])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), crimson),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return t

    # 2. خلاصه و هدف شغلی
    story.append(make_sec_header('خلاصه حرفه‌ای و اهداف کاری'))
    story.append(Spacer(1, 3))
    summary_text = (
        "دانشجوی کارشناسی حسابداری دانشگاه آزاد اسلامی تهران مرکزی و دانش‌آموخته دوره جامع حسابداری و سپیدار سیستم از مجتمع فنی تهران (MFT). "
        "برخوردار از تجارب عملی در حسابداری فروشگاهی، انبارداری و کنترل موجودی کالا (فروشگاه‌های آنلاین رویال دیجی و دی‌پی کامپیوتر)، حسابداری شرکت‌های گردشگری و همایشی، "
        "مدیریت و تسویه تنخواه‌گردان، ثبت دریافت‌ها و پرداخت‌ها و مغایرت‌گیری بانکی. فردی دقیق، منظم، با انضباط مالی بالا و علاقه‌مند به کار تیمی و توسعه راهکارهای نوین مالی."
    )
    story.append(Paragraph(fa(summary_text), body_style))
    story.append(Spacer(1, 6))

    # 3. سوابق شغلی
    story.append(make_sec_header('سوابق شغلی و تجارب اجرایی'))
    story.append(Spacer(1, 4))

    jobs = [
        {
            "role": "حسابدار مالی",
            "company": "شرکت زمان‌نما پویش مهراد",
            "date": "شهریور ۱۴۰۵ — آبان ۱۴۰۵",
            "tasks": [
                "ثبت و رسیدگی روزانه به اسناد مالی، کنترل صحت فاکتورها و بایگانی دفاتر مالی",
                "انجام مغایرت‌گیری بانکی دوره‌ای و کنترل حساب‌های تجاری طرف‌های حساب",
                "نظارت، مدیریت و تسویه هزینه‌ها و حساب‌های تنخواه‌گردان مجموعه"
            ]
        },
        {
            "role": "حسابدار و مسئول کنترل موجودی و انبارداری",
            "company": "فروشگاه‌های اینترنتی رویال دیجی و دی‌پی کامپیوتر (royaldigi.ir / dpcomputer.ir)",
            "date": "تیر ۱۴۰۵ — شهریور ۱۴۰۵",
            "tasks": [
                "حسابداری فروشگاهی، صدور فاکتور و تطبیق تسویه‌حساب درگاه‌های پرداخت آنلاین",
                "انبارگردانی ادواری، کنترل کاردکس کالا، بررسی مغایرت‌ها و کسری/اضافات انبار کالای دیجیتال",
                "ثبت اسناد دریافت و پرداخت طرف‌های تجاری و تأمین‌کنندگان قطعات کامپیوتر"
            ]
        },
        {
            "role": "حسابدار",
            "company": "شرکت خدمات مسافرتی و گردشگری سرزمین اساطیری",
            "date": "مرداد ۱۴۰۴ — آبان ۱۴۰۴",
            "tasks": [
                "ثبت اسناد مالی مربوط به تورها، اقامتگاه‌ها و تسویه‌حساب با آژانس‌های همکار",
                "مدیریت تنخواه هزینه‌های عملیاتی تورها و بررسی اسناد مثبته هزینه‌ای"
            ]
        },
        {
            "role": "ادمین و هماهنگ‌کننده اجرایی",
            "company": "شرکت همایشگران سام",
            "date": "اردیبهشت ۱۴۰۴ — آذر ۱۴۰۴",
            "tasks": [
                "هماهنگی امور اداری و اجرایی برگزاری سمینارها و همایش‌ها و پاسخگویی به مراجعین",
                "مستندسازی رویدادها، آرشیو دیجیتال اسناد و پیگیری قراردادهای کارفرمایان"
            ]
        },
        {
            "role": "کمک‌حسابدار و مسئول تنخواه‌گردان",
            "company": "مجموعه آموزشی و مهدکودک ققنوس",
            "date": "خرداد ۱۴۰۴ — آذر ۱۴۰۴",
            "tasks": [
                "ثبت و کنترل روزانه دریافت‌ها (شهریه) و پرداخت‌های جاری و هزینه‌های عملیاتی",
                "مدیریت کامل تنخواه‌گردان و ساماندهی فاکتورها و انجام مغایرت‌گیری بانکی"
            ]
        },
        {
            "role": "ادمین و مسئول امور اداری",
            "company": "انجمن صنفی آشپزان و سرآشپزان ایران",
            "date": "خرداد ۱۴۰۳ — دی ۱۴۰۳",
            "tasks": [
                "مدیریت دبیرخانه، تنظیم صورتجلسات و مکاتبات اداری، ساماندهی پرونده‌های اعضا"
            ]
        }
    ]

    for job in jobs:
        row_t = Table([
            [
                Paragraph(job["date"], item_date_style),
                Paragraph(f"<b>{fa(job['role'])}</b> | <font color='#1e2227'>{fa(job['company'])}</font>", item_title_style)
            ]
        ], colWidths=[140, 395])
        row_t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(row_t)
        for t in job["tasks"]:
            story.append(Paragraph(f"• {fa(t)}", bullet_style))
        story.append(Spacer(1, 2.5))

    story.append(Spacer(1, 3))

    # 4. تحصیلات و مدارک تخصصی
    story.append(make_sec_header('تحصیلات و دوره‌های تخصصی'))
    story.append(Spacer(1, 3))

    edu_data = [
        [
            Paragraph("در حال تحصیل (کارشناسی)", item_date_style),
            Paragraph(f"<b>{fa('کارشناسی حسابداری')}</b> — {fa('دانشگاه آزاد اسلامی، واحد تهران مرکزی (مجتمع سوهانک)')}", body_style)
        ],
        [
            Paragraph("گواهینامه رسمی", item_date_style),
            Paragraph(f"<b>{fa('دوره جامع حسابداری و نرم‌افزار سپیدار')}</b> — {fa('مجتمع فنی تهران (MFT)')}", body_style)
        ],
        [
            Paragraph("مهارت‌های هفتگانه", item_date_style),
            Paragraph(f"<b>{fa('گواهینامه تخصصی ICDL (اکسل مالی، ویندوز و آفیس)')}</b>", body_style)
        ]
    ]
    edu_table = Table(edu_data, colWidths=[120, 415])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 5))

    # 5. مهارت‌های تخصصی، نرم‌افزاری و زبان خارجی
    story.append(make_sec_header('مهارت‌های تخصصی، نرم‌افزارها و زبان خارجی'))
    story.append(Spacer(1, 3))

    st_list = [
        "<b>نرم‌افزارهای حسابداری:</b> سپیدار سیستم همکاران سیستم (پیشرفته) | هلو (مسلط) | شایگان سیستم (مسلط)",
        "<b>عملیات مالی:</b> ثبت دریافت و پرداخت | کنترل و مدیریت تنخواه‌گردان | مغایرت‌گیری بانکی | حسابداری انبار و انبارگردانی | تکالیف مالیاتی و اظهارنامه",
        "<b>مهارت‌های رایانه‌ای:</b> مهارت‌های هفتگانه ICDL | اکسل مالی پیشرفته (فرمول‌نویسی، توابع مالی و تطبیق اسناد) | یادگیری سریع سامانه‌های نوین",
        "<b>زبان انگلیسی (۱۴ سال سابقه آموزش پیوسته):</b> شنیداری (۴ از ۵) | خواندن و درک مطلب (۴ از ۵) | نگارش (۴ از ۵) | گفتاری و مکالمه (۳ از ۵)",
        "<b>شایستگی‌های فردی:</b> دقت و توجه بالا به ارقام و جزئیات | انضباط مالی و رازداری حرفه‌ای | مسئولیت‌پذیری و پیگیری مستمر | روحیه تعاملی و کار تیمی"
    ]

    for st in st_list:
        story.append(Paragraph(fa(st), body_style))
        story.append(Spacer(1, 1.5))

    doc.build(story)
    print(f"Generated PDF: {filename}")

if __name__ == '__main__':
    generate_executive_resume('Data/Parsa_Kodari_Resume.pdf')
    generate_executive_resume('Parsa_Kodari_Resume.pdf')
