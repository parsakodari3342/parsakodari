# -*- coding: utf-8 -*-
import base64
import os

with open('parsa.webp', 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

img_data_uri = f"data:image/webp;base64,{b64_img}"

html_content = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl" data-language="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>پارسا کدری | حسابدار و کارشناس امور مالی | Parsa Kodari</title>
    <meta name="description" content="وب‌سایت و پورتفولیو حرفه‌ای پارسا کدری — حسابدار و کارشناس امور مالی، مسلط به نرم‌افزارهای سپیدار، هلو، شایگان، انبارداری و ICDL.">
    <meta name="keywords" content="پارسا کدری, Parsa Kodari, حسابدار, حسابداری, سپیدار, هلو, مغایرت‌گیری, رزومه حسابدار, سعادت آباد تهران">
    <meta name="theme-color" content="#730f23">
    <link rel="canonical" href="https://parsakodari.ir/">
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    
    <!-- Open Graph Tags -->
    <meta property="og:title" content="پارسا کدری | حسابدار و کارشناس امور مالی | Parsa Kodari">
    <meta property="og:description" content="پورتفولیو و رزومه حرفه‌ای پارسا کدری — حسابدار، مسلط به سیستم‌های مالی، انبارداری و نرم‌افزارهای مالی.">
    <meta property="og:url" content="https://parsakodari.ir/">
    <meta property="og:type" content="website">
    <meta property="og:image" content="parsa.png">

    <!-- Fonts: Vazirmatn (FA), Inter (EN), Playfair Display (Logo/Monogram) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,700;1,700&family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

    <style>
        :root {{
            /* Palette: Crimson (زرشکی) & Silver-Gray (طوسی نقره‌ای) */
            --bg-deep: #e8ebf0;
            --bg-main: #f0f3f6;
            --bg-card: #ffffff;
            --bg-card-hover: #f7f9fb;
            --bg-card-subtle: #f4f6f9;
            
            /* Metallic Silver / Gray Accents */
            --silver-light: #e4e7ec;
            --silver-base: #b0aaaa;
            --silver-dark: #6e6868;
            --silver-border: #d4d9e2;
            --border-color: #dbe0e8;
            --border-hover: rgba(122, 18, 38, 0.45);
            
            /* Rich Deep Crimson / Maroon */
            --crimson-deep: #480914;
            --crimson: #730f23;
            --crimson-bright: #8a142c;
            --crimson-light: #a31c37;
            --crimson-hover: #b82341;
            --crimson-glow: rgba(115, 15, 35, 0.22);
            --crimson-subtle: rgba(115, 15, 35, 0.08);
            --crimson-border: rgba(115, 15, 35, 0.22);
            
            /* Typography */
            --text-main: #181c22;
            --text-secondary: #3c434f;
            --text-muted: #667282;
            --text-on-crimson: #ffffff;
            
            /* Shadows & Geometry */
            --shadow-subtle: 0 4px 16px rgba(0, 0, 0, 0.04);
            --shadow-card: 0 10px 30px rgba(28, 35, 45, 0.07);
            --shadow-glow: 0 8px 30px rgba(115, 15, 35, 0.15);
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-full: 9999px;
            
            --fa: 'Vazirmatn', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
            --en: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            --serif: 'Playfair Display', Georgia, serif;
            --transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1);
        }}

        /* Language Visibility Rules */
        [data-en] {{ display: none !important; }}
        html[data-language="en"] [data-en] {{ display: revert !important; }}
        html[data-language="en"] [data-fa] {{ display: none !important; }}

        /* Typography per language */
        html[data-language="fa"] body {{ font-family: var(--fa); line-height: 1.85; }}
        html[data-language="en"] body {{ font-family: var(--en); line-height: 1.65; }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
            -webkit-tap-highlight-color: transparent;
        }}

        html, body {{
            overflow-x: hidden;
            width: 100%;
        }}

        body {{
            background-color: var(--bg-main);
            color: var(--text-main);
            background-image: 
                radial-gradient(circle at 12% 15%, rgba(115, 15, 35, 0.04) 0%, transparent 45%),
                radial-gradient(circle at 88% 50%, rgba(176, 170, 170, 0.25) 0%, transparent 50%),
                radial-gradient(circle at 50% 90%, rgba(115, 15, 35, 0.03) 0%, transparent 45%);
            background-attachment: fixed;
        }}

        body.menu-open {{
            overflow: hidden;
        }}

        /* Subtle Background Grid */
        .grid-bg {{
            position: fixed;
            inset: 0;
            background-image: 
                linear-gradient(rgba(0, 0, 0, 0.025) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 0, 0, 0.025) 1px, transparent 1px);
            background-size: 60px 60px;
            z-index: -1;
            pointer-events: none;
        }}

        a {{
            text-decoration: none;
            color: inherit;
            transition: var(--transition);
        }}

        ul {{
            list-style: none;
        }}

        img {{
            max-width: 100%;
            height: auto;
            display: block;
        }}

        .container {{
            max-width: 1240px;
            margin: 0 auto;
            padding: 0 24px;
        }}

        /* Buttons */
        .btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 12px 26px;
            border-radius: var(--radius-full);
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            border: 1px solid transparent;
            line-height: 1;
            text-align: center;
            white-space: nowrap;
        }}

        .btn-primary {{
            background: linear-gradient(135deg, var(--crimson-bright) 0%, var(--crimson) 100%);
            color: var(--text-on-crimson);
            box-shadow: 0 4px 18px var(--crimson-glow);
        }}

        .btn-primary:hover {{
            background: linear-gradient(135deg, var(--crimson-hover) 0%, var(--crimson-bright) 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 22px rgba(115, 15, 35, 0.35);
            color: #ffffff;
        }}

        .btn-outline {{
            background: #ffffff;
            color: var(--text-main);
            border: 1.5px solid var(--silver-border);
            box-shadow: var(--shadow-subtle);
        }}

        .btn-outline:hover {{
            border-color: var(--crimson-bright);
            color: var(--crimson-bright);
            background: var(--bg-card-hover);
            transform: translateY(-2px);
        }}

        .btn-sm {{
            padding: 8px 16px;
            font-size: 0.85rem;
        }}

        .btn-block {{
            width: 100%;
        }}

        /* Header & Navigation */
        header {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: rgba(240, 243, 246, 0.96);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-color);
            box-shadow: 0 2px 14px rgba(0, 0, 0, 0.03);
            transition: var(--transition);
        }}

        .nav-container {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 76px;
            position: relative;
        }}

        /* Brand Logo (Upper Right in RTL) */
        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            flex-shrink: 0;
        }}

        .brand-logo-svg {{
            display: block;
            flex-shrink: 0;
            width: 58px;
            height: 36px;
        }}

        .brand-text h2 {{
            font-size: 1.12rem;
            font-weight: 700;
            color: var(--text-main);
            letter-spacing: 0.3px;
            line-height: 1.2;
        }}

        .brand-text p {{
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-top: 2px;
            font-weight: 500;
            white-space: nowrap;
        }}

        /* Desktop Nav Links */
        .nav-links {{
            display: flex;
            gap: 26px;
            align-items: center;
        }}

        .nav-links a {{
            font-size: 0.92rem;
            font-weight: 500;
            color: var(--text-secondary);
            position: relative;
            padding: 6px 0;
            transition: var(--transition);
        }}

        .nav-links a:hover, .nav-links a.active {{
            color: var(--crimson-bright);
        }}

        .nav-links a::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0%;
            height: 2px;
            background: var(--crimson-bright);
            transition: width 0.3s ease;
        }}

        .nav-links a:hover::after {{
            width: 100%;
        }}

        /* Header Controls: Lang, CV buttons, Hamburger */
        .header-controls {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-shrink: 0;
        }}

        .desktop-cv-actions {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        /* Language Toggle */
        .lang-group {{
            display: flex;
            border: 1px solid var(--silver-border);
            border-radius: var(--radius-full);
            overflow: hidden;
            background: #ffffff;
            padding: 2px;
            box-shadow: var(--shadow-subtle);
        }}

        .lang-btn {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 5px 12px;
            cursor: pointer;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            transition: var(--transition);
            border-radius: var(--radius-full);
            font-family: var(--en);
        }}

        .lang-btn.active {{
            background: var(--crimson);
            color: #ffffff;
            box-shadow: 0 2px 8px var(--crimson-glow);
        }}

        .lang-btn:hover:not(.active) {{
            color: var(--crimson);
            background: rgba(115, 15, 35, 0.05);
        }}

        /* Sleek 3-bar Hamburger Button */
        .hamburger {{
            display: none;
            width: 42px;
            height: 42px;
            background: #ffffff;
            border: 1px solid var(--silver-border);
            border-radius: 10px;
            cursor: pointer;
            padding: 10px 8px;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            transition: var(--transition);
            box-shadow: var(--shadow-subtle);
            z-index: 1002;
        }}

        .hamburger .bar {{
            width: 22px;
            height: 2px;
            background: var(--text-main);
            border-radius: 2px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .hamburger.active .bar:nth-child(1) {{
            transform: translateY(8px) rotate(45deg);
            background: var(--crimson-bright);
        }}

        .hamburger.active .bar:nth-child(2) {{
            opacity: 0;
            transform: scale(0.2);
        }}

        .hamburger.active .bar:nth-child(3) {{
            transform: translateY(-8px) rotate(-45deg);
            background: var(--crimson-bright);
        }}

        .mobile-cv-actions {{
            display: none;
        }}

        .nav-backdrop {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(18, 22, 28, 0.45);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            z-index: 998;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }}

        .nav-backdrop.active {{
            opacity: 1;
            pointer-events: auto;
        }}

        /* Hero Section */
        .hero {{
            padding: 145px 0 80px;
            min-height: 88vh;
            display: flex;
            align-items: center;
            position: relative;
        }}

        .hero-grid {{
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 60px;
            align-items: center;
        }}

        .hero-content .eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--crimson-bright);
            font-size: 0.88rem;
            font-weight: 600;
            padding: 6px 18px;
            border: 1px solid var(--crimson-border);
            border-radius: var(--radius-full);
            background: var(--crimson-subtle);
            margin-bottom: 24px;
        }}

        .eyebrow-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--crimson-bright);
            box-shadow: 0 0 10px var(--crimson-glow);
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0% {{ transform: scale(0.95); opacity: 0.8; }}
            50% {{ transform: scale(1.2); opacity: 1; }}
            100% {{ transform: scale(0.95); opacity: 0.8; }}
        }}

        .hero-content h1 {{
            font-size: clamp(2.1rem, 4vw, 3.4rem);
            font-weight: 800;
            color: var(--text-main);
            line-height: 1.3;
            margin-bottom: 20px;
            letter-spacing: -0.5px;
        }}

        .hero-content h1 span.crimson-text {{
            color: var(--crimson-bright);
            position: relative;
        }}

        .hero-content p.hero-desc {{
            font-size: 1.05rem;
            color: var(--text-secondary);
            margin-bottom: 32px;
            max-width: 95%;
            text-align: justify;
        }}

        .hero-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-bottom: 32px;
        }}

        .hero-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
            padding-top: 6px;
        }}

        .badge-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #ffffff;
            border: 1px solid var(--silver-border);
            color: var(--text-secondary);
            padding: 6px 16px;
            border-radius: var(--radius-full);
            font-size: 0.84rem;
            font-weight: 500;
            box-shadow: var(--shadow-subtle);
        }}

        .badge-pill svg {{
            color: var(--crimson-bright);
        }}

        /* Hero Visual & Portrait */
        .hero-visual {{
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .portrait-outer {{
            position: relative;
            width: 360px;
            height: 460px;
            border-radius: var(--radius-lg);
            padding: 7px;
            background: linear-gradient(145deg, var(--crimson-bright) 0%, #ffffff 40%, var(--silver-base) 100%);
            box-shadow: 0 18px 45px rgba(28, 35, 45, 0.12), 0 4px 20px rgba(115, 15, 35, 0.15);
            border: 1px solid var(--silver-border);
        }}

        .portrait-inner {{
            width: 100%;
            height: 100%;
            border-radius: calc(var(--radius-lg) - 5px);
            overflow: hidden;
            background: var(--bg-deep);
            position: relative;
        }}

        .portrait-inner img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center top;
            transition: transform 0.6s ease;
            display: block;
        }}

        .portrait-outer:hover .portrait-inner img {{
            transform: scale(1.03);
        }}

        /* Floating Info Badges on Hero Image (Desktop only) */
        .floating-badge {{
            position: absolute;
            background: rgba(255, 255, 255, 0.96);
            border: 1px solid var(--silver-border);
            backdrop-filter: blur(12px);
            padding: 12px 18px;
            border-radius: var(--radius-md);
            box-shadow: 0 10px 28px rgba(28, 35, 45, 0.1);
            display: flex;
            align-items: center;
            gap: 12px;
            z-index: 2;
        }}

        .fb-1 {{
            bottom: -20px;
            right: -25px;
            border-right: 3.5px solid var(--crimson-bright);
        }}

        html[dir="ltr"] .fb-1 {{
            right: auto;
            left: -25px;
            border-right: 1px solid var(--silver-border);
            border-left: 3.5px solid var(--crimson-bright);
        }}

        .fb-2 {{
            top: 25px;
            left: -25px;
            border-left: 3.5px solid var(--silver-dark);
        }}

        html[dir="ltr"] .fb-2 {{
            left: auto;
            right: -25px;
            border-left: 1px solid var(--silver-border);
            border-right: 3.5px solid var(--silver-dark);
        }}

        .floating-badge .fb-icon {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--crimson-subtle);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--crimson-bright);
        }}

        .floating-badge h4 {{
            font-size: 0.98rem;
            color: var(--text-main);
            font-weight: 700;
        }}

        .floating-badge p {{
            font-size: 0.76rem;
            color: var(--text-muted);
        }}

        /* Section Ornament */
        .section-divider {{
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--silver-border), transparent);
            margin: 60px 0;
        }}

        .section-header {{
            margin-bottom: 48px;
            text-align: center;
        }}

        .kicker {{
            color: var(--crimson-bright);
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            display: block;
            margin-bottom: 8px;
        }}

        .section-header h2 {{
            font-size: clamp(1.8rem, 3.5vw, 2.5rem);
            color: var(--text-main);
            font-weight: 700;
        }}

        .section-header p {{
            color: var(--text-muted);
            margin-top: 10px;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
            font-size: 1rem;
        }}

        /* About Section */
        .about-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 32px;
        }}

        .about-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 36px;
            box-shadow: var(--shadow-card);
            transition: var(--transition);
        }}

        .about-card:hover {{
            border-color: var(--border-hover);
            transform: translateY(-3px);
            box-shadow: 0 16px 36px rgba(28, 35, 45, 0.1);
        }}

        .about-card-icon {{
            width: 52px;
            height: 52px;
            border-radius: var(--radius-md);
            background: linear-gradient(135deg, rgba(115, 15, 35, 0.12), rgba(176, 170, 170, 0.15));
            border: 1px solid var(--crimson-border);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--crimson-bright);
            margin-bottom: 22px;
        }}

        .about-card h3 {{
            font-size: 1.35rem;
            margin-bottom: 14px;
            color: var(--text-main);
            font-weight: 700;
        }}

        .about-card p {{
            color: var(--text-secondary);
            font-size: 0.98rem;
            line-height: 1.85;
            text-align: justify;
        }}

        .traits-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: 10px;
        }}

        .trait-item {{
            background: var(--bg-card-subtle);
            border: 1px solid var(--silver-border);
            border-radius: var(--radius-sm);
            padding: 10px 14px;
            font-size: 0.88rem;
            color: var(--text-main);
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .trait-item svg {{
            color: var(--crimson-bright);
            flex-shrink: 0;
        }}

        /* Experience Timeline */
        .timeline {{
            position: relative;
            max-width: 980px;
            margin: 0 auto;
        }}

        .timeline::before {{
            content: '';
            position: absolute;
            top: 10px;
            bottom: 10px;
            right: 24px;
            width: 2px;
            background: linear-gradient(180deg, var(--crimson-bright), var(--silver-base), var(--border-color));
        }}

        html[dir="ltr"] .timeline::before {{
            right: auto;
            left: 24px;
        }}

        .timeline-item {{
            position: relative;
            padding-right: 64px;
            margin-bottom: 36px;
        }}

        html[dir="ltr"] .timeline-item {{
            padding-right: 0;
            padding-left: 64px;
        }}

        .timeline-dot {{
            position: absolute;
            top: 24px;
            right: 15px;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #ffffff;
            border: 4px solid var(--crimson-bright);
            box-shadow: 0 0 12px var(--crimson-glow);
            z-index: 2;
        }}

        html[dir="ltr"] .timeline-dot {{
            right: auto;
            left: 15px;
        }}

        .timeline-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 30px;
            box-shadow: var(--shadow-card);
            transition: var(--transition);
        }}

        .timeline-card:hover {{
            border-color: var(--border-hover);
            transform: translateX(-4px);
            box-shadow: 0 14px 34px rgba(28, 35, 45, 0.1);
        }}

        html[dir="ltr"] .timeline-card:hover {{
            transform: translateX(4px);
        }}

        .timeline-top {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            gap: 12px;
        }}

        .timeline-role {{
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        .timeline-company {{
            color: var(--crimson-bright);
            font-weight: 600;
            font-size: 1.02rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .timeline-date {{
            background: var(--bg-card-subtle);
            border: 1px solid var(--silver-border);
            color: var(--text-muted);
            padding: 4px 14px;
            border-radius: var(--radius-full);
            font-size: 0.84rem;
            font-weight: 500;
        }}

        .timeline-links {{
            display: flex;
            gap: 10px;
            margin: 10px 0 14px;
            flex-wrap: wrap;
        }}

        .website-link {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #ffffff;
            border: 1px solid var(--silver-border);
            padding: 4px 12px;
            border-radius: var(--radius-full);
            font-size: 0.82rem;
            color: var(--text-secondary);
            font-weight: 500;
            transition: var(--transition);
        }}

        .website-link:hover {{
            border-color: var(--crimson-bright);
            color: var(--crimson-bright);
            background: var(--bg-card-hover);
        }}

        .website-link svg {{
            color: var(--crimson-bright);
        }}

        .timeline-desc {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.8;
            margin-bottom: 14px;
            text-align: justify;
        }}

        .timeline-tasks {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}

        .timeline-tasks li {{
            font-size: 0.9rem;
            color: var(--text-secondary);
            position: relative;
            padding-right: 20px;
            line-height: 1.7;
        }}

        html[dir="ltr"] .timeline-tasks li {{
            padding-right: 0;
            padding-left: 20px;
        }}

        .timeline-tasks li::before {{
            content: '▪';
            position: absolute;
            right: 0;
            color: var(--crimson-bright);
            font-size: 1.2rem;
            line-height: 1;
        }}

        html[dir="ltr"] .timeline-tasks li::before {{
            right: auto;
            left: 0;
        }}

        /* ====================================================
           Skills Section (3-Column Grid + Round Numbers)
           ==================================================== */
        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 26px;
        }}

        .skill-group-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 30px 24px;
            box-shadow: var(--shadow-card);
            transition: var(--transition);
        }}

        .skill-group-card:hover {{
            border-color: var(--border-hover);
            transform: translateY(-4px);
            box-shadow: 0 14px 34px rgba(28, 35, 45, 0.1);
        }}

        .skill-group-header {{
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 22px;
            padding-bottom: 14px;
            border-bottom: 1px solid var(--silver-border);
        }}

        .skill-icon-wrap {{
            width: 46px;
            height: 46px;
            border-radius: var(--radius-md);
            background: var(--crimson-subtle);
            border: 1px solid var(--crimson-border);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--crimson-bright);
            flex-shrink: 0;
        }}

        .skill-group-header h3 {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        .skill-group-header p {{
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 2px;
        }}

        .skill-bars {{
            display: flex;
            flex-direction: column;
            gap: 18px;
        }}

        .skill-bar-item {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .skill-info {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .skill-info .name {{
            font-size: 0.92rem;
            font-weight: 600;
            color: var(--text-main);
        }}

        .skill-info .level {{
            color: var(--crimson-bright);
            font-size: 0.84rem;
            font-weight: 600;
        }}

        .skill-track {{
            height: 7px;
            width: 100%;
            background: var(--bg-deep);
            border-radius: var(--radius-full);
            overflow: hidden;
            border: 1px solid var(--silver-border);
        }}

        .skill-fill {{
            height: 100%;
            border-radius: var(--radius-full);
            background: linear-gradient(90deg, var(--crimson), var(--crimson-bright));
            transition: width 1.2s ease;
        }}

        /* English Language Scores Box */
        .lang-assessment-box {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 30px;
            box-shadow: var(--shadow-card);
            margin-top: 32px;
        }}

        .lang-skills-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-top: 14px;
        }}

        .lang-skill-card {{
            background: var(--bg-card-subtle);
            border: 1px solid var(--silver-border);
            border-radius: var(--radius-md);
            padding: 16px 18px;
        }}

        .lang-skill-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}

        .lang-skill-header .title {{
            font-weight: 600;
            font-size: 0.92rem;
            color: var(--text-main);
        }}

        .lang-skill-header .score {{
            font-weight: 700;
            color: var(--crimson-bright);
            font-size: 0.95rem;
        }}

        .dots-row {{
            display: flex;
            gap: 6px;
        }}

        .dot-score {{
            width: 13px;
            height: 13px;
            border-radius: 50%;
            background: var(--bg-deep);
            border: 1px solid var(--silver-border);
        }}

        .dot-score.filled {{
            background: var(--crimson-bright);
            border-color: var(--crimson);
            box-shadow: 0 2px 6px var(--crimson-glow);
        }}

        /* Education Section */
        .edu-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 32px;
        }}

        .edu-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 34px;
            box-shadow: var(--shadow-card);
            display: flex;
            gap: 22px;
            align-items: flex-start;
            transition: var(--transition);
        }}

        .edu-card:hover {{
            border-color: var(--border-hover);
            transform: translateY(-3px);
            box-shadow: 0 16px 36px rgba(28, 35, 45, 0.1);
        }}

        .edu-icon {{
            width: 54px;
            height: 54px;
            border-radius: var(--radius-md);
            background: var(--crimson-subtle);
            border: 1px solid var(--crimson-border);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--crimson-bright);
            flex-shrink: 0;
        }}

        .edu-info h3 {{
            font-size: 1.25rem;
            color: var(--text-main);
            margin-bottom: 8px;
            font-weight: 700;
        }}

        .edu-info h4 {{
            color: var(--crimson-bright);
            font-size: 0.98rem;
            font-weight: 600;
            margin-bottom: 10px;
        }}

        .edu-info p {{
            color: var(--text-secondary);
            font-size: 0.94rem;
            line-height: 1.8;
            margin-bottom: 12px;
        }}

        .edu-badge {{
            display: inline-block;
            background: var(--bg-card-subtle);
            border: 1px solid var(--silver-border);
            color: var(--text-muted);
            padding: 3px 12px;
            border-radius: var(--radius-full);
            font-size: 0.8rem;
            font-weight: 500;
        }}

        /* Contact Section */
        .contact-grid {{
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 36px;
        }}

        .contact-info-panel {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 40px;
            box-shadow: var(--shadow-card);
        }}

        .contact-info-panel h3 {{
            font-size: 1.5rem;
            color: var(--text-main);
            margin-bottom: 14px;
        }}

        .contact-info-panel p {{
            color: var(--text-secondary);
            font-size: 1.02rem;
            line-height: 1.8;
            margin-bottom: 28px;
        }}

        .contact-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 14px 18px;
            background: var(--bg-card-subtle);
            border: 1px solid var(--silver-border);
            border-radius: var(--radius-md);
            transition: var(--transition);
            text-decoration: none;
            color: inherit;
        }}

        .contact-item:hover {{
            border-color: var(--crimson-bright);
            background: #ffffff;
            transform: translateX(-4px);
            box-shadow: var(--shadow-subtle);
        }}

        html[dir="ltr"] .contact-item:hover {{
            transform: translateX(4px);
        }}

        .contact-item-icon {{
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: var(--crimson-subtle);
            border: 1px solid var(--crimson-border);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--crimson-bright);
            flex-shrink: 0;
        }}

        .contact-item-text .label {{
            font-size: 0.8rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 500;
            display: block;
            margin-bottom: 2px;
        }}

        .contact-item-text .val {{
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
            direction: ltr;
            text-align: left;
            display: inline-block;
            unicode-bidi: plaintext;
        }}

        html[dir="rtl"] .contact-item-text .val {{
            text-align: right;
        }}

        /* Contact Form */
        .contact-form-panel {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 40px;
            box-shadow: var(--shadow-card);
        }}

        .form-group {{
            margin-bottom: 20px;
        }}

        .form-group label {{
            display: block;
            margin-bottom: 8px;
            font-size: 0.88rem;
            color: var(--text-secondary);
            font-weight: 600;
        }}

        .form-group input, .form-group textarea {{
            width: 100%;
            padding: 13px 16px;
            background: var(--bg-card-subtle);
            border: 1px solid var(--silver-border);
            border-radius: var(--radius-sm);
            color: var(--text-main);
            font-family: inherit;
            font-size: 16px; /* Prevents auto-zoom in mobile Safari */
            transition: var(--transition);
        }}

        .form-group input:focus, .form-group textarea:focus {{
            outline: none;
            border-color: var(--crimson-bright);
            background: #ffffff;
            box-shadow: 0 0 0 3px var(--crimson-glow);
        }}

        .form-group textarea {{
            resize: vertical;
            min-height: 120px;
        }}

        /* Footer */
        footer {{
            background: #ffffff;
            border-top: 1px solid var(--border-color);
            padding: 50px 0 30px;
            margin-top: 80px;
        }}

        .footer-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 24px;
            padding-bottom: 30px;
            border-bottom: 1px solid var(--silver-border);
        }}

        .footer-links {{
            display: flex;
            gap: 24px;
        }}

        .footer-links a {{
            color: var(--text-muted);
            font-size: 0.92rem;
            font-weight: 500;
        }}

        .footer-links a:hover {{
            color: var(--crimson-bright);
        }}

        .footer-bottom {{
            padding-top: 22px;
            text-align: center;
            font-size: 0.88rem;
            color: var(--text-muted);
            font-weight: 500;
        }}

        /* Animations */
        .reveal {{
            opacity: 0;
            transform: translateY(24px);
            transition: all 0.7s cubic-bezier(0.5, 0, 0, 1);
        }}

        .reveal.active {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* Back to top button */
        .back-to-top {{
            position: fixed;
            bottom: 24px;
            left: 24px;
            width: 44px;
            height: 44px;
            background: #ffffff;
            border: 1px solid var(--silver-border);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--crimson-bright);
            box-shadow: 0 4px 16px rgba(0,0,0,0.12);
            cursor: pointer;
            z-index: 990;
            opacity: 0;
            visibility: hidden;
            transition: var(--transition);
        }}

        html[dir="ltr"] .back-to-top {{
            left: auto;
            right: 24px;
        }}

        .back-to-top.visible {{
            opacity: 1;
            visibility: visible;
        }}

        .back-to-top:hover {{
            background: var(--crimson-bright);
            color: #ffffff;
            border-color: var(--crimson-bright);
            transform: translateY(-3px);
        }}

        /* ====================================================
           RESPONSIVE BREAKPOINTS (Mobile & Tablet Optimization)
           ==================================================== */
        @media (max-width: 1024px) {{
            .skills-grid {{
                grid-template-columns: 1fr;
            }}

            .lang-skills-grid {{
                grid-template-columns: 1fr 1fr;
            }}
        }}

        @media (max-width: 920px) {{
            .nav-container {{
                height: 66px;
            }}

            .desktop-cv-actions {{
                display: none !important;
            }}

            .hamburger {{
                display: flex;
            }}

            .nav-backdrop {{
                display: block;
            }}

            .nav-links {{
                position: fixed;
                top: 66px;
                right: 0;
                left: 0;
                width: 100%;
                background: #ffffff;
                flex-direction: column;
                align-items: stretch;
                padding: 16px 20px 24px;
                border-bottom: 2px solid var(--crimson-border);
                box-shadow: 0 16px 36px rgba(0, 0, 0, 0.12);
                max-height: calc(100vh - 66px);
                overflow-y: auto;
                transform: translateY(-110%);
                opacity: 0;
                visibility: hidden;
                pointer-events: none;
                transition: transform 0.32s cubic-bezier(0.2, 0.9, 0.3, 1), opacity 0.25s ease, visibility 0.32s;
                z-index: 999;
                gap: 0;
            }}

            .nav-links.active {{
                transform: translateY(0);
                opacity: 1;
                visibility: visible;
                pointer-events: auto;
            }}

            .nav-links a {{
                padding: 14px 12px;
                font-size: 1.02rem;
                font-weight: 600;
                color: var(--text-main);
                border-bottom: 1px solid var(--bg-deep);
                display: flex;
                align-items: center;
                justify-content: space-between;
            }}

            .nav-links a::after {{
                display: none;
            }}

            .mobile-cv-actions {{
                display: flex;
                flex-direction: column;
                gap: 10px;
                margin-top: 18px;
                padding-top: 10px;
            }}

            .mobile-cv-actions .btn {{
                width: 100%;
                justify-content: center;
                padding: 12px 18px;
                font-size: 0.92rem;
            }}

            /* Hero on Tablet & Mobile */
            .hero {{
                padding: 95px 0 45px;
                min-height: auto;
            }}

            .hero-grid {{
                grid-template-columns: 1fr;
                gap: 28px;
                text-align: center;
            }}

            .hero-visual {{
                order: -1;
                margin-bottom: 4px;
            }}

            .portrait-outer {{
                width: 230px;
                height: 290px;
                margin: 0 auto;
                padding: 5px;
            }}

            .fb-1, .fb-2 {{
                display: none !important;
            }}

            .hero-content h1 {{
                font-size: clamp(1.65rem, 5.5vw, 2.25rem);
                margin-bottom: 14px;
            }}

            .hero-content p.hero-desc {{
                font-size: 0.96rem;
                line-height: 1.85;
                margin-left: auto;
                margin-right: auto;
                margin-bottom: 24px;
                text-align: justify;
            }}

            .hero-actions {{
                flex-direction: column;
                width: 100%;
                max-width: 340px;
                margin: 0 auto 24px;
                gap: 10px;
            }}

            .hero-actions .btn {{
                width: 100%;
                justify-content: center;
                padding: 13px 20px;
                font-size: 0.95rem;
            }}

            .hero-badges {{
                justify-content: center;
                gap: 8px;
            }}

            .badge-pill {{
                font-size: 0.78rem;
                padding: 5px 12px;
            }}

            /* Grids */
            .about-grid, .edu-grid, .contact-grid {{
                grid-template-columns: 1fr;
                gap: 20px;
            }}
        }}

        @media (max-width: 600px) {{
            .container {{
                padding: 0 16px;
            }}

            .section-header {{
                margin-bottom: 32px;
            }}

            .section-header h2 {{
                font-size: 1.45rem;
            }}

            .section-header p {{
                font-size: 0.92rem;
            }}

            /* Timeline Mobile */
            .timeline {{
                padding: 0;
            }}

            .timeline::before {{
                right: 14px;
            }}

            html[dir="ltr"] .timeline::before {{
                right: auto;
                left: 14px;
            }}

            .timeline-item {{
                padding-right: 36px;
                padding-left: 0;
                margin-bottom: 20px;
            }}

            html[dir="ltr"] .timeline-item {{
                padding-right: 0;
                padding-left: 36px;
            }}

            .timeline-dot {{
                right: 5px;
                top: 20px;
                width: 18px;
                height: 18px;
                border-width: 3px;
            }}

            html[dir="ltr"] .timeline-dot {{
                right: auto;
                left: 5px;
            }}

            .timeline-card {{
                padding: 18px 16px;
                border-radius: 14px;
            }}

            .timeline-top {{
                flex-direction: column;
                align-items: flex-start;
                gap: 6px;
            }}

            .timeline-role {{
                font-size: 1.05rem;
            }}

            .timeline-company {{
                font-size: 0.92rem;
            }}

            .timeline-date {{
                align-self: flex-start;
                font-size: 0.78rem;
                padding: 3px 10px;
                margin-top: 4px;
            }}

            .timeline-desc {{
                font-size: 0.88rem;
                line-height: 1.75;
            }}

            .timeline-tasks li {{
                font-size: 0.85rem;
                line-height: 1.7;
            }}

            .website-link {{
                font-size: 0.78rem;
                padding: 4px 10px;
            }}

            /* About & Skills & Education */
            .traits-grid, .lang-skills-grid {{
                grid-template-columns: 1fr;
                gap: 10px;
            }}

            .about-card, .edu-card, .skill-group-card, .contact-form-panel, .contact-info-panel, .lang-assessment-box {{
                padding: 22px 16px;
                border-radius: 16px;
            }}

            .contact-item {{
                padding: 12px 14px;
                gap: 12px;
            }}

            .contact-item-icon {{
                width: 38px;
                height: 38px;
            }}

            .contact-item-text .val {{
                font-size: 0.95rem;
            }}

            .brand-text p.brand-sub {{
                display: none; /* Keeps top header 100% clean on small phones */
            }}

            .footer-container {{
                flex-direction: column;
                text-align: center;
                gap: 20px;
            }}

            .footer-links {{
                flex-wrap: wrap;
                justify-content: center;
                gap: 14px;
            }}
        }}
    </style>
</head>
<body>
    <div class="grid-bg"></div>

    <!-- Header Navigation -->
    <header id="mainHeader">
        <div class="container nav-container">
            <!-- Brand & PK Logo (Upper Right in RTL) -->
            <a href="#" class="brand">
                <svg width="58" height="36" viewBox="0 0 240 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="brand-logo-svg">
                    <text x="15" y="106" font-family="'Playfair Display', Georgia, serif" font-size="110" font-weight="700" fill="#730f23">P</text>
                    <text x="74" y="106" font-family="'Playfair Display', Georgia, serif" font-size="110" font-weight="700" fill="#6e6868">K</text>
                    <line x1="195" y1="22" x2="195" y2="118" stroke="#8a8585" stroke-width="5" stroke-linecap="round" />
                </svg>
                <div class="brand-text">
                    <h2 data-fa>پارسا کدری</h2>
                    <h2 data-en>Parsa Kodari</h2>
                    <p class="brand-sub" data-fa>حسابدار و کارشناس امور مالی</p>
                    <p class="brand-sub" data-en>Accountant & Financial Specialist</p>
                </div>
            </a>

            <!-- Header Controls: Lang Switcher, Desktop CV buttons & Hamburger -->
            <div class="header-controls">
                <!-- Language Toggle (Always Visible) -->
                <div class="lang-group">
                    <button class="lang-btn active" data-lang="fa">FA</button>
                    <button class="lang-btn" data-lang="en">EN</button>
                </div>

                <!-- Desktop Action Buttons (Hidden on mobile <= 920px) -->
                <div class="desktop-cv-actions">
                    <a href="resume.html" target="_blank" class="btn btn-outline btn-sm">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                        <span data-fa>نسخه وب رزومه</span>
                        <span data-en>Web Resume</span>
                    </a>
                    <a href="Parsa_Kodari_Resume.pdf" class="btn btn-primary btn-sm" download="Parsa_Kodari_Resume.pdf">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        <span data-fa>دانلود رزومه (PDF)</span>
                        <span data-en>Download CV (PDF)</span>
                    </a>
                </div>

                <!-- Hamburger Button (Visible on mobile <= 920px) -->
                <button class="hamburger" id="menuToggle" aria-label="منوی ناوبری">
                    <span class="bar"></span>
                    <span class="bar"></span>
                    <span class="bar"></span>
                </button>
            </div>

            <!-- Nav Links Drawer (Desktop inline / Mobile slide-down) -->
            <nav class="nav-links" id="navLinks">
                <a href="#about" data-fa>درباره من</a>
                <a href="#about" data-en>About</a>

                <a href="#experience" data-fa>سوابق شغلی</a>
                <a href="#experience" data-en>Experience</a>

                <a href="#skills" data-fa>مهارت‌ها</a>
                <a href="#skills" data-en>Skills</a>

                <a href="#education" data-fa>تحصیلات و مدارک</a>
                <a href="#education" data-en>Education</a>

                <a href="#contact" data-fa>تماس با من</a>
                <a href="#contact" data-en>Contact</a>

                <!-- Mobile-Only CV Actions inside Drawer -->
                <div class="mobile-cv-actions">
                    <a href="Parsa_Kodari_Resume.pdf" class="btn btn-primary btn-sm btn-block" download="Parsa_Kodari_Resume.pdf">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        <span data-fa>دانلود فایل کامل رزومه (PDF)</span>
                        <span data-en>Download Full Resume (PDF)</span>
                    </a>
                    <a href="resume.html" target="_blank" class="btn btn-outline btn-sm btn-block">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                        <span data-fa>مشاهده نسخه وب رزومه</span>
                        <span data-en>View Web Resume</span>
                    </a>
                </div>
            </nav>
        </div>
        <div class="nav-backdrop" id="navBackdrop"></div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container hero-grid">
            <div class="hero-content reveal">
                <span class="eyebrow">
                    <span class="eyebrow-dot"></span>
                    <span data-fa>حسابدار و کارشناس امور مالی | متولد ۲۰۰۶</span>
                    <span data-en>Accountant & Financial Specialist | Born 2006</span>
                </span>

                <h1 data-fa>
                    سلام، من <span class="crimson-text">پارسا کدری</span> هستم<br>
                    <span>دقت در ارقام، انضباط در مدیریت مالی</span>
                </h1>
                <h1 data-en>
                    Hi, I'm <span class="crimson-text">Parsa Kodari</span><br>
                    <span>Precision in Numbers, Excellence in Finance</span>
                </h1>

                <p class="hero-desc" data-fa>
                    دانشجوی کارشناسی حسابداری دانشگاه آزاد اسلامی واحد تهران مرکزی (سوهانک) با گواهینامه حسابداری از مجتمع فنی تهران و مدرک سپیدار. برخوردار از تجارب عملی مؤثر در حسابداری فروشگاهی، انبارداری و کنترل موجودی کالا در وب‌سایت‌های رویال دیجی و دی‌پی کامپیوتر، شرکت‌های بازرگانی و گردشگری، مدیریت تنخواه، مغایرت‌گیری و ساماندهی اسناد مالی.
                </p>
                <p class="hero-desc" data-en>
                    Accounting student at Islamic Azad University, Central Tehran Branch) certified in Comprehensive Accounting and Sepidar ERP software by Tehran Technical Complex (MFT). Hands-on experience in commercial & e-commerce accounting, inventory control at RoyalDigi & DP Computer, petty cash oversight, bank reconciliation, and financial reporting.
                </p>

                <div class="hero-actions">
                    <a href="Parsa_Kodari_Resume.pdf" class="btn btn-primary" download="Parsa_Kodari_Resume.pdf">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        <span data-fa>دانلود رزومه کامل (PDF)</span>
                        <span data-en>Download Full CV (PDF)</span>
                    </a>
                    <a href="#experience" class="btn btn-outline">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                        <span data-fa>سوابق شغلی</span>
                        <span data-en>Experience</span>
                    </a>
                </div>

                <div class="hero-badges">
                    <div class="badge-pill">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>سپیدار سیستم</span>
                        <span data-en>Sepidar System</span>
                    </div>
                    <div class="badge-pill">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>هلو و شایگان</span>
                        <span data-en>Holo & Shaygan</span>
                    </div>
                    <div class="badge-pill">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>انبارداری و مغایرت‌گیری</span>
                        <span data-en>Inventory & Audit</span>
                    </div>
                    <div class="badge-pill">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>مهارت‌های هفتگانه ICDL</span>
                        <span data-en>ICDL Certified</span>
                    </div>
                </div>
            </div>

            <!-- Hero Portrait (Base64 WebP + Floating Badges on Desktop) -->
            <div class="hero-visual reveal">
                <div class="portrait-outer">
                    <div class="portrait-inner">
                        <img src="{img_data_uri}" alt="پارسا کدری — Parsa Kodari">
                    </div>
                </div>

                <!-- Desktop Floating Badges -->
                <div class="floating-badge fb-1">
                    <div class="fb-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
                    </div>
                    <div>
                        <h4 data-fa>دانشجوی حسابداری</h4>
                        <h4 data-en>Undergraduate Accounting Student</h4>
                        <p data-fa>دانشگاه آزاد واحد تهران مرکزی</p>
                        <p data-en>IAU Central Tehran Branch</p>
                    </div>
                </div>

                <div class="floating-badge fb-2">
                    <div class="fb-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                    </div>
                    <div>
                        <h4 data-fa>مدرک مجتمع فنی تهران</h4>
                        <h4 data-en>Tehran Technical Complex</h4>
                        <p data-fa>حسابداری جامع و سپیدار</p>
                        <p data-en>Comprehensive Accounting & ERP</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Divider -->
    <div class="container"><div class="section-divider"></div></div>

    <!-- About Me & Professional Profile -->
    <section id="about" class="container">
        <div class="section-header reveal">
            <span class="kicker" data-fa>درباره من و اهداف شغلی</span>
            <span class="kicker" data-en>ABOUT ME & OBJECTIVES</span>
            <h2 data-fa>رویکرد حرفه‌ای و انضباط مالی</h2>
            <h2 data-en>Professional Approach & Values</h2>
            <p data-fa>تعهد به صحت اطلاعات، رازداری کاری، یادگیری پویا و ایجاد نظم ساختارمند در فرآیندهای مالی و حسابداری سازمان</p>
            <p data-en>Commitment to data integrity, professional confidentiality, rapid learning, and structured financial processes</p>
        </div>

        <div class="about-grid">
            <div class="about-card reveal">
                <div class="about-card-icon">
                    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                </div>
                <h3 data-fa>شناسنامه حرفه‌ای</h3>
                <h3 data-en>Professional Identity</h3>
                <p data-fa>
                    اینجانب <strong>پارسا کدری</strong>، متولد سال ۲۰۰۶ (۱۳۸۴)، دانشجوی رشته حسابداری در دانشگاه آزاد اسلامی واحد تهران مرکزی (سوهانک) هستم. با انگیزه بالا، اشتیاق به یادگیری مداوم و دیدگاهی سیستماتیک، تلاش کرده‌ام از ابتدای مسیر تحصیلی، دانش تئوریک را با تجارب واقعی محیط‌های کسب‌وکار درآمیزم. کار با دفاتر تجاری، نرم‌افزارهای یکپارچه مالی، فرآیندهای خرید و فروش، کنترل موجودی کالا و رفع مغایرت‌های بانکی و تنخواه از حوزه‌های تمرکز من است.
                </p>
                <p data-en>
                    I am <strong>Parsa Kodari</strong>, born in 2006, an undergraduate accounting student at Islamic Azad University Central Tehran Branch (Sohanak). Driven by dedication and strong analytical interest, I bridge academic accounting theories with real-world business operations. My background covers retail and corporate accounting, ERP implementations, sales-purchase tracking, inventory auditing, petty cash administration, and bank reconciliation.
                </p>
            </div>

            <div class="about-card reveal">
                <div class="about-card-icon">
                    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                </div>
                <h3 data-fa>ارزش‌های کاری و اصول انضباطی</h3>
                <h3 data-en>Core Work Ethics & Strengths</h3>
                <p data-fa>
                    در دنیای حسابداری، دقت در ثبت کوچک‌ترین ارقام ضامن سلامت تصمیم‌گیری‌های کلان مدیریتی است. مهم‌ترین اصول کاری من عبارتند از:
                </p>
                <p data-en>
                    In financial management, precision in the smallest transaction secures the foundation of strategic business decisions. My working values include:
                </p>

                <div class="traits-grid">
                    <div class="trait-item">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>دقت و توجه عمیق به جزئیات</span>
                        <span data-en>Attention to Detail</span>
                    </div>
                    <div class="trait-item">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>نظم و ساختارمندی اسناد</span>
                        <span data-en>Document Structuring</span>
                    </div>
                    <div class="trait-item">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>رازداری و امانتداری مالی</span>
                        <span data-en>Confidentiality & Trust</span>
                    </div>
                    <div class="trait-item">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>سرعت عمل در یادگیری نرم‌افزارها</span>
                        <span data-en>Fast Software Adaptability</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Divider -->
    <div class="container"><div class="section-divider"></div></div>

    <!-- Work Experience Section -->
    <section id="experience" class="container">
        <div class="section-header reveal">
            <span class="kicker" data-fa>تجارب شغلی و اجرایی</span>
            <span class="kicker" data-en>WORK EXPERIENCE</span>
            <h2 data-fa>سوابق حرفه‌ای در حسابداری و عملیات</h2>
            <h2 data-en>Professional Career & Operations</h2>
            <p data-fa>مرور سوابق کاری و مسئولیت‌های اجرایی در شرکت‌های بازرگانی، فروشگاه‌های آنلاین، موسسات خدماتی و گردشگری</p>
            <p data-en>Overview of professional roles and achievements in commercial firms, e-commerce stores, tourism, and services</p>
        </div>

        <div class="timeline">
            <!-- 1. زمان نما پویش مهراد -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>حسابدار مالی و انبار</div>
                            <div class="timeline-role" data-en>Financial & Inventory Accountant</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
                                <span data-fa>شرکت زمان نما پویش مهراد</span>
                                <span data-en>Zaman Nama Pooyesh Mehrad Co.</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>شهریور ۱۴۰۴ — آبان ۱۴۰۴ (برج ۶ تا ۸ امسال)</span>
                        <span class="timeline-date" data-en>Aug 2025 — Oct 2025</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        ثبت و کنترل اسناد حسابداری، بررسی حساب‌های دریافتنی و پرداختنی، صدور فاکتورهای فروش و اسناد خرید، مغایرت‌گیری ماهانه حساب‌های بانکی و ساماندهی بایگانی مالی شرکت.
                    </p>
                    <p class="timeline-desc" data-en>
                        Bookkeeping and ledger entry recording, monitoring accounts payable and receivable, issuing purchase and sales vouchers, conducting monthly bank reconciliations, and systematizing the fiscal archive.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>صدور اسناد حسابداری دوبل و اسناد دریافت/پرداخت با نرم‌افزارهای مالی</li>
                        <li data-en>Recording double-entry accounting transactions and disbursement/collection receipts</li>
                        <li data-fa>کنترل روزانه گردش وجوه نقد، تنخواه‌گردان و صورتحساب‌های بانکی</li>
                        <li data-fa>پیگیری مطالبات، بررسی صورتحساب مشتریان و رفع سریع مغایرت‌ها</li>
                    </ul>
                </div>
            </div>

            <!-- 2. رویال دیجی و دی پی کامپیوتر -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>مسئول انبارداری و حسابداری فروشگاهی</div>
                            <div class="timeline-role" data-en>Inventory Supervisor & Store Accountant</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                                <span data-fa>رویال دیجی و دی‌پی کامپیوتر</span>
                                <span data-en>RoyalDigi & DP Computer</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>تیر ۱۴۰۴ — شهریور ۱۴۰۴ (برج ۴ تا ۶ امسال)</span>
                        <span class="timeline-date" data-en>Jun 2025 — Aug 2025</span>
                    </div>

                    <div class="timeline-links">
                        <a href="https://royaldigi.ir/" target="_blank" rel="noopener" class="website-link">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                            <span>royaldigi.ir</span>
                        </a>
                        <a href="https://dpcomputer.ir/" target="_blank" rel="noopener" class="website-link">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                            <span>dpcomputer.ir</span>
                        </a>
                    </div>

                    <p class="timeline-desc" data-fa>
                        مدیریت انبار قطعات دیجیتال و سخت‌افزار، ثبت ورود و خروج کالا در سیستم، انبارگردانی دوره‌ای، صدور فاکتورهای فروشگاهی آنلاین و مدیریت تراز فیزیکی و سیستمی موجودی کالا.
                    </p>
                    <p class="timeline-desc" data-en>
                        Supervision of tech hardware and digital components inventory, real-time logging of stock inflows/outflows, periodic stocktaking, e-commerce invoice management, and continuous inventory reconciliation.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>کنترل موجودی اقلام دیجیتال و سخت‌افزار و مغایرت‌گیری انبار فیزیکی با سیستم</li>
                        <li data-en>Inventory control for computer hardware and reconciliation of physical stock with ERP</li>
                        <li data-fa>ثبت اسناد خرید، حواله انبار، فاکتورهای فروش و مرجوعی‌های کالا</li>
                        <li data-en>Recording purchase orders, warehouse transfer slips, customer sales receipts, and returns</li>
                        <li data-fa>همکاری با بخش فروش اینترنتی رویال دیجی و دی‌پی کامپیوتر جهت به‌روزرسانی موجودی و قیمت‌ها</li>
                        <li data-en>Collaboration with online store teams to maintain accurate inventory levels and price books</li>
                    </ul>
                </div>
            </div>

            <!-- 3. شرکت گردشگری سرزمین اساطیری -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>حسابدار عمومی و تنخواه</div>
                            <div class="timeline-role" data-en>General & Petty Cash Accountant</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                                <span data-fa>شرکت گردشگری سرزمین اساطیری</span>
                                <span data-en>Sarzamin Asatiri Tourism Co.</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>مرداد ۱۴۰۴ — آبان ۱۴۰۴ (برج ۵ تا ۸ ۱۴۰۴)</span>
                        <span class="timeline-date" data-en>Jul 2025 — Oct 2025</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        حسابداری امور تورها و خدمات گردشگری، کنترل تنخواه‌گردان، تسویه حساب لیدرها و پیمانکاران، و بایگانی و تنظیم اسناد مالی مربوطه.
                    </p>
                    <p class="timeline-desc" data-en>
                        Tour services accounting, petty cash control, settlements with guides and contractors, and comprehensive financial archiving.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>رسیدگی به تنخواه‌گردان و اسناد هزینه‌ای روزمره شرکت</li>
                        <li data-en>Auditing petty cash expenditures and daily operational expense claims</li>
                        <li data-fa>کنترل حساب‌های فی‌مابین آژانس‌ها، هتل‌ها و پیمانکاران ترابری</li>
                        <li data-en>Reconciling inter-company accounts with travel agencies, hotels, and transport services</li>
                        <li data-fa>تهیه گزارش‌های ماهانه هزینه‌ها و درآمدها برای مدیریت</li>
                        <li data-en>Preparing monthly income and expense summaries for executive management</li>
                    </ul>
                </div>
            </div>

            <!-- 4. شرکت همایشگران سام -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>ادمین هماهنگی و پشتیبانی اجرایی</div>
                            <div class="timeline-role" data-en>Event Operations & Administration Officer</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <span data-fa>شرکت همایشگران سام</span>
                                <span data-en>Hamayeshgaran Sam Co.</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>اردیبهشت ۱۴۰۴ — آذر ۱۴۰۴ (برج ۲ تا ۹ ۱۴۰۴)</span>
                        <span class="timeline-date" data-en>Apr 2025 — Nov 2025</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        پشتیبانی اداری و مالی برگزاری سمینارها و رویدادها، هماهنگی شرکت‌کنندگان، ثبت نام و پیگیری واریزی‌ها و امور دبیرخانه‌ای.
                    </p>
                    <p class="timeline-desc" data-en>
                        Administrative and operations support for corporate conferences, attendee registration, fee collection tracking, and secretariat coordination.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>ثبت مشخصات شرکت‌کنندگان و تطبیق فیش‌های واریزی با حساب بانکی شرکت</li>
                        <li data-en>Registering conference delegates and verifying payment deposits against bank statements</li>
                        <li data-fa>پاسخگویی به مراجعین و هماهنگی تدارکات رویدادها و نشست‌ها</li>
                        <li data-en>Managing inquiries, vendor relations, and logistical arrangements for events</li>
                    </ul>
                </div>
            </div>

            <!-- 5. مهد کودک ققنوس -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>کمک حسابدار و مسئول مالی</div>
                            <div class="timeline-role" data-en>Assistant Accountant</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 15h-2v-6h2zm0-8h-2V7h2z"></path></svg>
                                <span data-fa>مهد کودک ققنوس</span>
                                <span data-en>Ghoghnous Educational Center</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>خرداد ۱۴۰۴ — آذر ۱۴۰۴ (برج ۳ تا ۹ ۱۴۰۴)</span>
                        <span class="timeline-date" data-en>May 2025 — Nov 2025</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        ثبت و کنترل روزانه دریافت‌ها و پرداخت‌ها، ثبت و مدیریت تنخواه، انجام مغایرت‌گیری و ساماندهی اسناد مالی مجموعه.
                    </p>
                    <p class="timeline-desc" data-en>
                        Recording daily collections and disbursements, monitoring petty cash operations, performing reconciliation, and organizing ledger files.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>ثبت و کنترل دقیق دریافت‌های شهریه و پرداختی‌های جاری مجموعه</li>
                        <li data-en>Recording and auditing tuition fees, payroll receipts, and routine disbursements</li>
                        <li data-fa>مدیریت کامل تنخواه‌گردان و اسناد هزینه‌ای روزمره</li>
                        <li data-en>Full administration of daily petty cash accounts and expense verification</li>
                        <li data-fa>انجام مغایرت‌گیری حساب‌ها و بررسی و رفع سریع اختلافات مالی</li>
                        <li data-en>Monthly account reconciliation and dispute resolution in financial records</li>
                    </ul>
                </div>
            </div>

            <!-- 6. انجمن صنفی آشپزان و سرآشپزان ایران -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>ادمین و مسئول هماهنگی امور اداری</div>
                            <div class="timeline-role" data-en>Administrative & Member Affairs Officer</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                                <span data-fa>انجمن صنفی آشپزان و سرآشپزان ایران</span>
                                <span data-en>Guild Association of Chefs of Iran</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>خرداد ۱۴۰۳ — دی ۱۴۰۳</span>
                        <span class="timeline-date" data-en>May 2024 — Dec 2024</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        مدیریت دبیرخانه، هماهنگی امور اعضا، بایگانی پرونده‌ها و تنظیم صورتجلسات و مکاتبات اداری انجمن.
                    </p>
                    <p class="timeline-desc" data-en>
                        Secretariat coordination, member registry management, official correspondence, and meeting minutes documentation.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>ثبت و پیگیری امور حق عضویت و صدور مدارک صنفی اعضا</li>
                        <li data-en>Registering membership fees, processing renewals, and issuing certificates</li>
                        <li data-fa>هماهنگی نشست‌ها و سمینارهای صنف و مدیریت دبیرخانه</li>
                        <li data-en>Organizing guild committee meetings, drafting official letters, and archiving</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Divider -->
    <div class="container"><div class="section-divider"></div></div>

    <!-- Skills & Tools Section (3 Cards with Completely Round Numbers) -->
    <section id="skills" class="container">
        <div class="section-header reveal">
            <span class="kicker" data-fa>مهارت‌های تخصصی و نرم‌افزارها</span>
            <span class="kicker" data-en>TECHNICAL SKILLS & TOOLS</span>
            <h2 data-fa>تسلط نرم‌افزاری و عملیات حسابداری</h2>
            <h2 data-en>Software Mastery & Financial Operations</h2>
            <p data-fa>به‌کارگیری به‌روزترین نرم‌افزارهای مالی، استانداردهای ثبت اسناد، حسابداری انبار و مهارت‌های کامپیوتری</p>
            <p data-en>Hands-on proficiency with financial ERP systems, bookkeeping standards, inventory control, and digital tools</p>
        </div>

        <div class="skills-grid">
            <!-- Group 1: Accounting Software -->
            <div class="skill-group-card reveal">
                <div class="skill-group-header">
                    <div class="skill-icon-wrap">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    </div>
                    <div>
                        <h3 data-fa>نرم‌افزارهای حسابداری</h3>
                        <h3 data-en>Accounting Software</h3>
                        <p data-fa>سامانه‌های مالی و اداری</p>
                        <p data-en>Financial & ERP Systems</p>
                    </div>
                </div>

                <div class="skill-bars">
                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>سپیدار سیستم (Sepidar)</span>
                            <span class="name" data-en>Sepidar ERP</span>
                            <span class="level" data-fa>پیشرفته (۹۵٪)</span>
                            <span class="level" data-en>Advanced (95%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 95%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>نرم‌افزار هلو (Holo)</span>
                            <span class="name" data-en>Holo Accounting</span>
                            <span class="level" data-fa>مسلط (۸۵٪)</span>
                            <span class="level" data-en>Proficient (85%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 85%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>شایگان سیستم (Shaygan)</span>
                            <span class="name" data-en>Shaygan System</span>
                            <span class="level" data-fa>مسلط (۸۵٪)</span>
                            <span class="level" data-en>Proficient (85%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 85%;"></div></div>
                    </div>
                </div>
            </div>

            <!-- Group 2: Financial Operations -->
            <div class="skill-group-card reveal" style="transition-delay: 0.1s">
                <div class="skill-group-header">
                    <div class="skill-icon-wrap">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"></rect><line x1="12" y1="8" x2="12" y2="12"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
                    </div>
                    <div>
                        <h3 data-fa>عملیات مالی و خزانه‌داری</h3>
                        <h3 data-en>Treasury & Financial Ops</h3>
                        <p data-fa>فرآیندهای پولی و کنترلی</p>
                        <p data-en>Reconciliation & Petty Cash</p>
                    </div>
                </div>

                <div class="skill-bars">
                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>ثبت دریافت‌ها و پرداخت‌ها</span>
                            <span class="name" data-en>Receipts & Payments</span>
                            <span class="level" data-fa>تخصصی (۹۵٪)</span>
                            <span class="level" data-en>Expert (95%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 95%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>مدیریت و کنترل تنخواه‌گردان</span>
                            <span class="name" data-en>Petty Cash Oversight</span>
                            <span class="level" data-fa>تخصصی (۹۰٪)</span>
                            <span class="level" data-en>Expert (90%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 90%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>مغایرت‌گیری بانکی و حساب‌ها</span>
                            <span class="name" data-en>Bank Reconciliation</span>
                            <span class="level" data-fa>پیشرفته (۹۰٪)</span>
                            <span class="level" data-en>Advanced (90%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 90%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>انبارداری و کنترل موجودی کالا</span>
                            <span class="name" data-en>Inventory & Stock Audit</span>
                            <span class="level" data-fa>مسلط (۹۰٪)</span>
                            <span class="level" data-en>Proficient (90%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 90%;"></div></div>
                    </div>
                </div>
            </div>

            <!-- Group 3: Computer & ICDL -->
            <div class="skill-group-card reveal" style="transition-delay: 0.2s">
                <div class="skill-group-header">
                    <div class="skill-icon-wrap">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                    </div>
                    <div>
                        <h3 data-fa>مهارت‌های فناوری و ICDL</h3>
                        <h3 data-en>IT & ICDL Expertise</h3>
                        <p data-fa>نرم‌افزارهای اداری و داده‌ها</p>
                        <p data-en>Spreadsheets & Systems</p>
                    </div>
                </div>

                <div class="skill-bars">
                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>اکسل مالی و فرمول‌نویسی</span>
                            <span class="name" data-en>Financial Excel & Formulas</span>
                            <span class="level" data-fa>پیشرفته (۹۰٪)</span>
                            <span class="level" data-en>Advanced (90%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 90%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>مهارت‌های هفتگانه ICDL</span>
                            <span class="name" data-en>Comprehensive ICDL Suite</span>
                            <span class="level" data-fa>مسلط (۹۰٪)</span>
                            <span class="level" data-en>Proficient (90%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 90%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>امور مالیاتی و اظهارنامه (مقدماتی)</span>
                            <span class="name" data-en>Tax Basics & Returns</span>
                            <span class="level" data-fa>خوب (۷۵٪)</span>
                            <span class="level" data-en>Good (75%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 75%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>یادگیری سریع ابزارهای دیجیتال</span>
                            <span class="name" data-en>Fast Digital Adaptability</span>
                            <span class="level" data-fa>عالی (۹۵٪)</span>
                            <span class="level" data-en>Excellent (95%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 95%;"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- English Language Proficiency (4/5 and 3/5 with dots) -->
        <div class="lang-assessment-box reveal">
            <div class="skill-group-header" style="margin-bottom: 16px; border-bottom: none; padding-bottom: 0;">
                <div class="skill-icon-wrap">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                </div>
                <div>
                    <h3 data-fa>ارزیابی تسلط به زبان انگلیسی</h3>
                    <h3 data-en>English Language Proficiency</h3>
                    <p data-fa>سنجش مهارت‌های چهارگانه زبان (بر اساس درخواست رسمی)</p>
                    <p data-en>Four-skill linguistic assessment</p>
                </div>
            </div>

            <div class="lang-skills-grid">
                <!-- Listening -->
                <div class="lang-skill-card">
                    <div class="lang-skill-header">
                        <span class="title" data-fa>شنیداری (Listening)</span>
                        <span class="title" data-en>Listening</span>
                        <span class="score">4 / 5</span>
                    </div>
                    <div class="dots-row">
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score"></div>
                    </div>
                </div>

                <!-- Reading -->
                <div class="lang-skill-card">
                    <div class="lang-skill-header">
                        <span class="title" data-fa>درک مطلب (Reading)</span>
                        <span class="title" data-en>Reading</span>
                        <span class="score">4 / 5</span>
                    </div>
                    <div class="dots-row">
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score"></div>
                    </div>
                </div>

                <!-- Writing -->
                <div class="lang-skill-card">
                    <div class="lang-skill-header">
                        <span class="title" data-fa>نگارش (Writing)</span>
                        <span class="title" data-en>Writing</span>
                        <span class="score">4 / 5</span>
                    </div>
                    <div class="dots-row">
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score"></div>
                    </div>
                </div>

                <!-- Speaking -->
                <div class="lang-skill-card">
                    <div class="lang-skill-header">
                        <span class="title" data-fa>مکالمه (Speaking)</span>
                        <span class="title" data-en>Speaking</span>
                        <span class="score">3 / 5</span>
                    </div>
                    <div class="dots-row">
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score filled"></div>
                        <div class="dot-score"></div>
                        <div class="dot-score"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Divider -->
    <div class="container"><div class="section-divider"></div></div>

    <!-- Education & Certifications Section -->
    <section id="education" class="container">
        <div class="section-header reveal">
            <span class="kicker" data-fa>سوابق تحصیلی و دوره‌های تخصصی</span>
            <span class="kicker" data-en>EDUCATION & CERTIFICATIONS</span>
            <h2 data-fa>پشتوانه علمی و مدارک حرفه‌ای</h2>
            <h2 data-en>Academic Credentials & Certifications</h2>
            <p data-fa>ترکیب دانش آکادمیک دانشگاهی در رشته حسابداری با مدارک رسمی و مهارت‌آموزی در مراکز معتبر آموزشی</p>
            <p data-en>Combining university degree studies in accounting with accredited vocational certifications</p>
        </div>

        <div class="edu-grid">
            <div class="edu-card reveal">
                <div class="edu-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
                </div>
                <div class="edu-info">
                    <h3 data-fa>کارشناسی حسابداری (در حال تحصیل)</h3>
                    <h3 data-en>B.Sc. in Accounting (Undergraduate)</h3>
                    <h4 data-fa>دانشگاه آزاد اسلامی واحد تهران مرکزی (سوهانک)</h4>
                    <h4 data-en>Islamic Azad University, Central Tehran Branch</h4>
                    <p data-fa>دانشجوی مقطع کارشناسی حسابداری. تمرکز بر مبانی حسابداری مالی، حسابداری صنعتی، قوانین مالیاتی، استانداردهای حسابرسی و سیستم‌های اطلاعاتی حسابداری.</p>
                    <p data-en>Undergraduate studies focusing on Financial Accounting, Cost Accounting, Tax Laws, Auditing Standards, and Accounting Information Systems.</p>
                    <span class="edu-badge" data-fa>ورودی مهر ۱۴۰۲ — در حال تحصیل</span>
                    <span class="edu-badge" data-en>Enrolled Sep 2023 — In Progress</span>
                </div>
            </div>

            <div class="edu-card reveal">
                <div class="edu-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                </div>
                <div class="edu-info">
                    <h3 data-fa>دوره جامع حسابداری و نرم‌افزار سپیدار</h3>
                    <h3 data-en>Comprehensive Accounting & Sepidar ERP</h3>
                    <h4 data-fa>مجتمع فنی تهران (MFT)</h4>
                    <h4 data-en>Tehran Technical Complex (MFT)</h4>
                    <p data-fa>گذراندن دوره رسمی حسابداری کاربردی، ثبت دفاتر قانونی، بهای تمام‌شده، مغایرت‌گیری، کار با ماژول‌های خرید و فروش، انبار و خزانه‌داری در نرم‌افزار سپیدار.</p>
                    <p data-en>Accredited certification in applied commercial accounting, legal ledger bookkeeping, cost calculation, and full modules of Sepidar ERP (Purchases, Sales, Inventory, Treasury).</p>
                    <span class="edu-badge" data-fa>گواهینامه رسمی و بین‌المللی</span>
                    <span class="edu-badge" data-en>Certified Credential</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Divider -->
    <div class="container"><div class="section-divider"></div></div>

    <!-- Contact Section -->
    <section id="contact" class="container">
        <div class="section-header reveal">
            <span class="kicker" data-fa>راه‌های ارتباطی</span>
            <span class="kicker" data-en>GET IN TOUCH</span>
            <h2 data-fa>آماده همکاری و گفتگوهای کاری</h2>
            <h2 data-en>Let's Connect & Collaborate</h2>
            <p data-fa>برای هماهنگی مصاحبه شغلی، همکاری‌های مالی و حسابداری، پروژه‌های انبارداری یا مشاوره از طریق راه‌های زیر در ارتباط باشید</p>
            <p data-en>Reach out for career opportunities, financial consulting, accounting collaborations, or inventory audit projects</p>
        </div>

        <div class="contact-grid">
            <div class="contact-info-panel reveal">
                <h3 data-fa>اطلاعات تماس مستقیم</h3>
                <h3 data-en>Direct Contact Details</h3>
                <p data-fa>مشتاق بررسی فرصت‌های شغلی جدید در حوزه حسابداری، کنترل موجودی و امور مالی هستم. پاسخگوی تماس‌ها و پیام‌های شما خواهم بود.</p>
                <p data-en>I welcome discussions regarding prospective accounting, bookkeeping, and inventory roles. Feel free to connect directly.</p>

                <div class="contact-list">
                    <!-- Phone -->
                    <a href="tel:09034443342" class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>شماره تماس مستقیم</span>
                            <span class="label" data-en>Phone Number</span>
                            <span class="val">09034443342</span>
                        </div>
                    </a>

                    <!-- Email -->
                    <a href="mailto:Parsa.kodari@gmail.com" class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>پست الکترونیکی (ایمیل)</span>
                            <span class="label" data-en>Email Address</span>
                            <span class="val">Parsa.kodari@gmail.com</span>
                        </div>
                    </a>

                    <!-- Instagram -->
                    <a href="https://instagram.com/Parsa___kodari" target="_blank" rel="noopener" class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>صفحه کاری اینستاگرام</span>
                            <span class="label" data-en>Instagram Profile</span>
                            <span class="val">@Parsa___kodari</span>
                        </div>
                    </a>

                    <!-- Location -->
                    <div class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>موقعیت مکانی</span>
                            <span class="label" data-en>Location</span>
                            <span class="val" style="direction: rtl;" data-fa>تهران، سعادت‌آباد</span>
                            <span class="val" style="direction: ltr;" data-en>Sa'adat Abad, Tehran, Iran</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Contact Form -->
            <div class="contact-form-panel reveal">
                <h3 data-fa>ارسال پیام سریع (پیامک مستقیم)</h3>
                <h3 data-en>Send a Quick Direct Message</h3>
                <p data-fa>فرم زیر را تکمیل کنید تا پیام شما مستقیماً در قالب پیامک (SMS) ارسال گردد.</p>
                <p data-en>Fill out the form below to initiate an immediate SMS correspondence.</p>

                <form id="contactForm">
                    <div class="form-group">
                        <label for="cName" data-fa>نام و نام خانوادگی:</label>
                        <label for="cName" data-en>Your Full Name:</label>
                        <input type="text" id="cName" required placeholder="مثال: علیرضا محمدی">
                    </div>
                    <div class="form-group">
                        <label for="cPhone" data-fa>شماره تماس یا ایمیل:</label>
                        <label for="cPhone" data-en>Phone / Email:</label>
                        <input type="text" id="cPhone" required placeholder="مثال: 09123456789">
                    </div>
                    <div class="form-group">
                        <label for="cMessage" data-fa>متن پیام شما:</label>
                        <label for="cMessage" data-en>Message Content:</label>
                        <textarea id="cMessage" required placeholder="شرح پیام یا پیشنهاد همکاری..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        <span data-fa>ارسال پیامک مستقیم</span>
                        <span data-en>Send Direct SMS</span>
                    </button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container footer-container">
            <div class="brand">
                <svg width="50" height="32" viewBox="0 0 240 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="brand-logo-svg">
                    <text x="15" y="106" font-family="'Playfair Display', Georgia, serif" font-size="110" font-weight="700" fill="#730f23">P</text>
                    <text x="74" y="106" font-family="'Playfair Display', Georgia, serif" font-size="110" font-weight="700" fill="#6e6868">K</text>
                    <line x1="195" y1="22" x2="195" y2="118" stroke="#8a8585" stroke-width="5" stroke-linecap="round" />
                </svg>
                <div class="brand-text">
                    <h2 data-fa>پارسا کدری</h2>
                    <h2 data-en>Parsa Kodari</h2>
                    <p data-fa>حسابدار و کارشناس امور مالی</p>
                    <p data-en>Accountant & Financial Specialist</p>
                </div>
            </div>

            <div class="footer-links">
                <a href="#about" data-fa>درباره من</a>
                <a href="#about" data-en>About</a>
                <a href="#experience" data-fa>سوابق شغلی</a>
                <a href="#experience" data-en>Experience</a>
                <a href="#skills" data-fa>مهارت‌ها</a>
                <a href="#skills" data-en>Skills</a>
                <a href="resume.html" target="_blank" data-fa>نسخه وب رزومه</a>
                <a href="resume.html" target="_blank" data-en>Web Resume</a>
                <a href="Parsa_Kodari_Resume.pdf" download data-fa>دانلود PDF</a>
                <a href="Parsa_Kodari_Resume.pdf" download data-en>Download PDF</a>
            </div>
        </div>
        <div class="container footer-bottom">
            <p data-fa>© 2026 پارسا کدری — تمامی حقوق محفوظ است | parsakodari.ir</p>
            <p data-en>© 2026 Parsa Kodari — All Rights Reserved | parsakodari.ir</p>
        </div>
    </footer>

    <!-- Back to top button -->
    <button class="back-to-top" id="backToTop" aria-label="بازگشت به بالا">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"></polyline></svg>
    </button>

    <script>
        // --- Multi-Language Toggle (FA / EN) ---
        function setLanguage(lang) {{
            document.documentElement.setAttribute('data-language', lang);
            document.documentElement.dir = (lang === 'fa') ? 'rtl' : 'ltr';
            document.documentElement.lang = lang;
            
            document.querySelectorAll('.lang-btn').forEach(btn => {{
                btn.classList.toggle('active', btn.dataset.lang === lang);
            }});
            
            if (lang === 'en') {{
                document.title = "Parsa Kodari | Accountant & Financial Specialist | Portfolio";
            }} else {{
                document.title = "پارسا کدری | حسابدار و کارشناس امور مالی | Parsa Kodari";
            }}
        }}

        document.querySelectorAll('.lang-btn').forEach(btn => {{
            btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
        }});

        // --- Mobile Navigation Menu Drawer ---
        const menuToggle = document.getElementById('menuToggle');
        const navLinks = document.getElementById('navLinks');
        const navBackdrop = document.getElementById('navBackdrop');

        function toggleMenu() {{
            const isOpen = navLinks.classList.contains('active');
            if (isOpen) {{
                closeMenu();
            }} else {{
                openMenu();
            }}
        }}

        function openMenu() {{
            menuToggle.classList.add('active');
            navLinks.classList.add('active');
            navBackdrop.classList.add('active');
            document.body.classList.add('menu-open');
        }}

        function closeMenu() {{
            menuToggle.classList.remove('active');
            navLinks.classList.remove('active');
            navBackdrop.classList.remove('active');
            document.body.classList.remove('menu-open');
        }}

        menuToggle.addEventListener('click', toggleMenu);
        navBackdrop.addEventListener('click', closeMenu);

        document.querySelectorAll('.nav-links a, .mobile-cv-actions a').forEach(link => {{
            link.addEventListener('click', closeMenu);
        }});

        // --- Back to top button on scroll ---
        const backToTopBtn = document.getElementById('backToTop');
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 400) {{
                backToTopBtn.classList.add('visible');
            }} else {{
                backToTopBtn.classList.remove('visible');
            }}
        }});

        backToTopBtn.addEventListener('click', () => {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }});

        // --- Scroll Reveal Animations ---
        const observerOptions = {{
            threshold: 0.1,
            rootMargin: "0px 0px -30px 0px"
        }};
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }}
            }});
        }}, observerOptions);

        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

        // --- Direct SMS Form Submission ---
        document.getElementById('contactForm').addEventListener('submit', function(e) {{
            e.preventDefault();
            const name = document.getElementById('cName').value.trim();
            const phone = document.getElementById('cPhone').value.trim();
            const message = document.getElementById('cMessage').value.trim();
            const smsBody = encodeURIComponent(`پیام از سایت parsakodari.ir:\\nنام: ${{name}}\\nشماره تماس: ${{phone}}\\nپیام: ${{message}}`);
            window.location.href = `sms:09034443342?body=${{smsBody}}`;
        }});

        // Default language: Persian
        setLanguage('fa');
    </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully regenerated index.html with 3-column skills and clean round numbers!")
