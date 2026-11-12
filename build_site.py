import base64

with open('parsa.webp', 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

img_data_uri = f"data:image/webp;base64,{b64_img}"

html_content = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl" data-language="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>پارسا کدری | حسابدار و کارشناس امور مالی | Parsa Kodari</title>
    <meta name="description" content="وب‌سایت و پورتفولیو حرفه‌ای پارسا کدری — حسابدار و کارشناس امور مالی، مسلط به نرم‌افزارهای سپیدار، هلو، شایگان، انبارداری و ICDL.">
    <meta name="keywords" content="پارسا کدری, Parsa Kodari, حسابدار, حسابداری, سپیدار, هلو, مغایرت‌گیری, رزومه حسابدار, سعادت آباد تهران">
    <meta name="theme-color" content="#edf0f4">
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
            /* Surface & Backgrounds */
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
        }}

        body {{
            background-color: var(--bg-main);
            color: var(--text-main);
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 12% 15%, rgba(115, 15, 35, 0.04) 0%, transparent 45%),
                radial-gradient(circle at 88% 50%, rgba(176, 170, 170, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 50% 90%, rgba(115, 15, 35, 0.03) 0%, transparent 45%);
            background-attachment: fixed;
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
            padding: 12px 28px;
            border-radius: var(--radius-full);
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            transition: var(--transition);
            border: 1px solid transparent;
            text-decoration: none;
        }}

        .btn-primary {{
            background: linear-gradient(135deg, var(--crimson-bright) 0%, var(--crimson) 100%);
            color: #ffffff;
            box-shadow: 0 6px 20px var(--crimson-glow);
        }}

        .btn-primary:hover {{
            background: linear-gradient(135deg, var(--crimson-hover) 0%, var(--crimson-bright) 100%);
            transform: translateY(-2px);
            box-shadow: 0 10px 26px rgba(115, 15, 35, 0.35);
            color: #ffffff;
        }}

        .btn-outline {{
            background: #ffffff;
            color: var(--text-main);
            border: 1px solid var(--silver-border);
            box-shadow: var(--shadow-subtle);
        }}

        .btn-outline:hover {{
            background: var(--bg-card-hover);
            border-color: var(--crimson-bright);
            color: var(--crimson-bright);
            transform: translateY(-2px);
        }}

        .btn-sm {{
            padding: 8px 18px;
            font-size: 0.85rem;
        }}

        /* Header & Navigation */
        header {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 100;
            background: rgba(240, 243, 246, 0.94);
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
            height: 84px;
        }}

        /* Brand Logo (Upper Right in RTL) */
        .brand {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .brand-logo-svg {{
            display: block;
            flex-shrink: 0;
        }}

        .brand-text h2 {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-main);
            letter-spacing: 0.3px;
        }}

        .brand-text p {{
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-top: 1px;
            font-weight: 500;
        }}

        .nav-links {{
            display: flex;
            gap: 28px;
            align-items: center;
        }}

        .nav-links a {{
            font-size: 0.92rem;
            font-weight: 500;
            color: var(--text-secondary);
            position: relative;
            padding: 6px 0;
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

        .header-actions {{
            display: flex;
            align-items: center;
            gap: 12px;
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
            padding: 6px 14px;
            cursor: pointer;
            font-size: 0.82rem;
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

        .hamburger {{
            display: none;
            background: none;
            border: none;
            color: var(--text-main);
            font-size: 1.6rem;
            cursor: pointer;
        }}

        /* Hero Section */
        .hero {{
            padding: 155px 0 85px;
            min-height: 90vh;
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
            font-size: clamp(2.3rem, 4.2vw, 3.6rem);
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
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-bottom: 34px;
            max-width: 95%;
            text-align: justify;
        }}

        .hero-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-bottom: 34px;
        }}

        .hero-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
            padding-top: 8px;
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
            width: 370px;
            height: 470px;
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

        /* Floating Info Badges on Hero Image */
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
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 28px 0;
            opacity: 0.6;
        }}

        .section-divider::before,
        .section-divider::after {{
            content: '';
            height: 1px;
            width: 120px;
            background: linear-gradient(90deg, transparent, var(--silver-border), transparent);
        }}

        .section-divider i {{
            width: 7px;
            height: 7px;
            background: var(--crimson);
            transform: rotate(45deg);
            margin: 0 16px;
        }}

        /* Sections Common */
        section {{
            padding: 85px 0;
            position: relative;
        }}

        .section-header {{
            margin-bottom: 48px;
            text-align: center;
        }}

        .kicker {{
            color: var(--crimson-bright);
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 12px;
            display: inline-block;
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

        /* About & Objective Section */
        .about-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }}

        .about-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 38px;
            transition: var(--transition);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: var(--shadow-card);
        }}

        .about-card:hover {{
            border-color: var(--border-hover);
            transform: translateY(-4px);
            box-shadow: 0 16px 36px rgba(28, 35, 45, 0.1);
        }}

        .about-card h3 {{
            font-size: 1.35rem;
            color: var(--text-main);
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .about-card h3 svg {{
            color: var(--crimson-bright);
        }}

        .about-card p {{
            color: var(--text-secondary);
            font-size: 1.02rem;
            line-height: 1.9;
            text-align: justify;
            margin-bottom: 22px;
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
            padding: 12px 16px;
            border-radius: var(--radius-md);
            font-size: 0.9rem;
            color: var(--text-secondary);
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 500;
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
            box-shadow: 0 0 10px var(--crimson-glow);
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
            font-size: 0.86rem;
            color: var(--text-secondary);
            background: #ffffff;
            border: 1px solid var(--silver-border);
            padding: 4px 12px;
            border-radius: var(--radius-sm);
            font-weight: 500;
        }}

        .website-link:hover {{
            color: #ffffff;
            background: var(--crimson);
            border-color: var(--crimson);
        }}

        .timeline-desc {{
            color: var(--text-secondary);
            font-size: 0.98rem;
            line-height: 1.85;
            margin-bottom: 14px;
        }}

        .timeline-tasks {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 7px;
        }}

        .timeline-tasks li {{
            position: relative;
            padding-right: 20px;
            font-size: 0.93rem;
            color: var(--text-secondary);
        }}

        html[dir="ltr"] .timeline-tasks li {{
            padding-right: 0;
            padding-left: 20px;
        }}

        .timeline-tasks li::before {{
            content: '▪';
            position: absolute;
            right: 4px;
            color: var(--crimson-bright);
            font-size: 1.1rem;
            line-height: 1;
        }}

        html[dir="ltr"] .timeline-tasks li::before {{
            right: auto;
            left: 4px;
        }}

        /* Skills Section */
        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 26px;
        }}

        .skill-group-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 30px 26px;
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
        }}

        .skill-group-header h3 {{
            font-size: 1.18rem;
            color: var(--text-main);
        }}

        .skill-group-header p {{
            font-size: 0.8rem;
            color: var(--text-muted);
        }}

        .skill-bars {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .skill-bar-item .skill-info {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 6px;
            font-size: 0.91rem;
            font-weight: 500;
        }}

        .skill-info .name {{
            color: var(--text-secondary);
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

        /* Language Assessment Box */
        .lang-section {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 38px;
            margin-top: 36px;
            box-shadow: var(--shadow-card);
        }}

        .lang-grid {{
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 38px;
            align-items: center;
        }}

        .lang-meta h3 {{
            font-size: 1.4rem;
            color: var(--text-main);
            margin-bottom: 12px;
        }}

        .lang-meta p {{
            color: var(--text-secondary);
            font-size: 0.98rem;
            line-height: 1.8;
            margin-bottom: 16px;
        }}

        .lang-tag {{
            display: inline-block;
            background: var(--crimson-subtle);
            border: 1px solid var(--crimson-border);
            color: var(--crimson-bright);
            padding: 4px 14px;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 600;
        }}

        .lang-skills-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 18px;
        }}

        .lang-skill-card {{
            background: var(--bg-card-subtle);
            border: 1px solid var(--silver-border);
            border-radius: var(--radius-md);
            padding: 16px 20px;
        }}

        .lang-skill-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}

        .lang-skill-header span.title {{
            font-weight: 600;
            color: var(--text-main);
            font-size: 0.94rem;
        }}

        .lang-skill-header span.score {{
            font-weight: 700;
            color: var(--crimson-bright);
            font-size: 0.95rem;
        }}

        .dots-row {{
            display: flex;
            gap: 6px;
        }}

        .dot-score {{
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: #ffffff;
            border: 2px solid var(--silver-border);
        }}

        .dot-score.filled {{
            background: var(--crimson-bright);
            border-color: var(--crimson-bright);
            box-shadow: 0 0 6px var(--crimson-glow);
        }}

        /* Education & Certifications */
        .edu-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }}

        .edu-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 34px;
            transition: var(--transition);
            display: flex;
            gap: 22px;
            box-shadow: var(--shadow-card);
        }}

        .edu-card:hover {{
            border-color: var(--border-hover);
            transform: translateY(-4px);
            box-shadow: 0 14px 34px rgba(28, 35, 45, 0.1);
        }}

        .edu-icon-wrap {{
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
        }}

        .contact-item-text .val {{
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
            direction: ltr;
            text-align: left;
            display: block;
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
            font-weight: 600;
            color: var(--text-main);
        }}

        .form-control {{
            width: 100%;
            background: #ffffff;
            border: 1px solid var(--silver-border);
            border-radius: var(--radius-sm);
            padding: 13px 16px;
            color: var(--text-main);
            font-family: inherit;
            font-size: 0.95rem;
            transition: var(--transition);
        }}

        .form-control:focus {{
            outline: none;
            border-color: var(--crimson-bright);
            box-shadow: 0 0 0 3px var(--crimson-glow);
        }}

        textarea.form-control {{
            min-height: 120px;
            resize: vertical;
        }}

        .form-btn {{
            width: 100%;
            padding: 14px;
            font-size: 1.02rem;
        }}

        /* Footer */
        footer {{
            background: #e4e7ec;
            border-top: 1px solid var(--silver-border);
            padding: 45px 0 30px;
            margin-top: 60px;
        }}

        .footer-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
            padding-bottom: 26px;
            border-bottom: 1px solid var(--silver-border);
        }}

        .footer-brand {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .footer-socials {{
            display: flex;
            gap: 12px;
        }}

        .social-link {{
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: #ffffff;
            border: 1px solid var(--silver-border);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            box-shadow: var(--shadow-subtle);
            transition: var(--transition);
        }}

        .social-link:hover {{
            background: var(--crimson);
            color: #ffffff;
            border-color: var(--crimson);
            transform: translateY(-2px);
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
            transform: translateY(26px);
            transition: all 0.75s cubic-bezier(0.5, 0, 0, 1);
        }}

        .reveal.active {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {{
            .hero-grid {{ grid-template-columns: 1fr; gap: 48px; text-align: center; }}
            .hero-content p.hero-desc {{ margin-left: auto; margin-right: auto; }}
            .hero-actions, .hero-badges {{ justify-content: center; }}
            .skills-grid {{ grid-template-columns: 1fr; }}
            .lang-grid {{ grid-template-columns: 1fr; }}
        }}

        @media (max-width: 820px) {{
            .nav-links {{
                position: fixed;
                top: 84px;
                left: 0;
                width: 100%;
                background: #ffffff;
                flex-direction: column;
                padding: 30px 0;
                border-bottom: 1px solid var(--border-color);
                box-shadow: 0 10px 30px rgba(0,0,0,0.08);
                clip-path: polygon(0 0, 100% 0, 100% 0, 0 0);
                transition: var(--transition);
            }}
            .nav-links.active {{
                clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
            }}
            .hamburger {{ display: block; }}
            .about-grid, .edu-grid, .contact-grid {{ grid-template-columns: 1fr; }}
            .portrait-outer {{ width: 290px; height: 380px; }}
            .fb-1, .fb-2 {{ display: none; }}
        }}

        @media (max-width: 540px) {{
            .traits-grid, .lang-skills-grid {{ grid-template-columns: 1fr; }}
            .hero {{ padding: 130px 0 60px; }}
            .contact-form-panel, .contact-info-panel, .about-card, .edu-card {{ padding: 24px 18px; }}
        }}
    </style>
</head>
<body>
    <div class="grid-bg"></div>

    <!-- Header Navigation -->
    <header>
        <div class="container nav-container">
            <!-- Brand & PK Logo (Upper Right in RTL) -->
            <a href="#" class="brand">
                <svg width="68" height="42" viewBox="0 0 240 140" fill="none" xmlns="http://www.w3.org/2000/svg" class="brand-logo-svg">
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
            </a>

            <!-- Mobile Hamburger -->
            <button class="hamburger" aria-label="Toggle Menu">☰</button>

            <!-- Nav Links -->
            <nav class="nav-links">
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
            </nav>

            <!-- Actions: Language & CV -->
            <div class="header-actions">
                <div class="lang-group">
                    <button class="lang-btn active" data-lang="fa">FA</button>
                    <button class="lang-btn" data-lang="en">EN</button>
                </div>
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
        </div>
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
                    دانشجوی ترم پنجم کارشناسی حسابداری دانشگاه آزاد اسلامی واحد تهران مرکزی (سوهانک) با گواهینامه حسابداری از مجتمع فنی تهران و مدرک سپیدار. برخوردار از تجارب عملی مؤثر در حسابداری فروشگاهی، انبارداری و کنترل موجودی کالا در وب‌سایت‌های رویال دیجی و دی‌پی کامپیوتر، شرکت‌های بازرگانی و گردشگری، مدیریت تنخواه، مغایرت‌گیری و ساماندهی اسناد مالی.
                </p>
                <p class="hero-desc" data-en>
                    Accounting student (5th semester at Islamic Azad University, Central Tehran Branch) certified in Comprehensive Accounting and Sepidar ERP software by Tehran Technical Complex (MFT). Hands-on experience in commercial & e-commerce accounting, inventory control at RoyalDigi & DP Computer, petty cash oversight, bank reconciliation, and financial reporting.
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
                    <a href="#contact" class="btn btn-outline">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                        <span data-fa>ارتباط با من</span>
                        <span data-en>Contact Me</span>
                    </a>
                </div>

                <div class="hero-badges">
                    <span class="badge-pill">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>سپیدار سیستم</span>
                        <span data-en>Sepidar ERP</span>
                    </span>
                    <span class="badge-pill">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>هلو و شایگان</span>
                        <span data-en>Holo & Shaygan</span>
                    </span>
                    <span class="badge-pill">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>انبارداری و مغایرت‌گیری</span>
                        <span data-en>Inventory & Reconciliation</span>
                    </span>
                    <span class="badge-pill">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span data-fa>مهارت‌های هفتگانه ICDL</span>
                        <span data-en>ICDL Specialist</span>
                    </span>
                </div>
            </div>

            <!-- Hero Portrait (Direct Base64 URI - 100% Reliable, Zero Network Latency) -->
            <div class="hero-visual reveal">
                <div class="portrait-outer">
                    <div class="portrait-inner">
                        <img src="{img_data_uri}" alt="پارسا کدری — Parsa Kodari">
                    </div>
                </div>

                <!-- Floating Badges -->
                <div class="floating-badge fb-1">
                    <div class="fb-icon">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
                    </div>
                    <div>
                        <h4 data-fa>دانشجوی ترم ۵ حسابداری</h4>
                        <h4 data-en>B.Sc. Accounting (5th Sem)</h4>
                        <p data-fa>دانشگاه آزاد واحد تهران مرکزی</p>
                        <p data-en>Islamic Azad University Central</p>
                    </div>
                </div>

                <div class="floating-badge fb-2">
                    <div class="fb-icon">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                    </div>
                    <div>
                        <h4 data-fa>مدرک مجتمع فنی تهران</h4>
                        <h4 data-en>MFT Certified</h4>
                        <p data-fa>حسابداری جامع و سپیدار</p>
                        <p data-en>Accounting & Sepidar</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <div class="section-divider"><i></i></div>

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
                <div>
                    <h3>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                        <span data-fa>خلاصه پروفایل حرفه‌ای</span>
                        <span data-en>Professional Profile</span>
                    </h3>
                    <p data-fa>
                        من پارسا کدری، متولد سال ۲۰۰۶ در تهران (سعادت‌آباد) هستم. مسیر حرفه‌ای خود را بر پایه علاقه عمیق به تحلیل‌های مالی، حسابداری مدرن و انضباط آماری پایه‌گذاری کرده‌ام. با تلفیق آموزش‌های دانشگاهی در رشته حسابداری و گذراندن دوره‌های تخصصی در مجتمع فنی تهران، توانسته‌ام تسلط کاملی بر نرم‌افزارهای حسابداری استاندارد کشور از جمله سپیدار، هلو و شایگان سیستم به دست آورم.
                    </p>
                    <p data-en>
                        I am Parsa Kodari, born in 2006 in Tehran (Sa'adat Abad). I have built my professional foundation on financial analysis, modern accounting systems, and analytical precision. Combining my academic studies in accounting with professional certifications from Tehran Technical Complex (MFT), I have gained strong expertise in leading accounting platforms including Sepidar, Holo, and Shaygan System.
                    </p>
                </div>
                <div>
                    <h4 style="color: var(--text-main); margin-bottom: 12px; font-size: 0.95rem; font-weight: 700;" data-fa>ویژگی‌های کلیدی فردی و رفتاری:</h4>
                    <h4 style="color: var(--text-main); margin-bottom: 12px; font-size: 0.95rem; font-weight: 700;" data-en>Key Personal Strengths:</h4>
                    <div class="traits-grid">
                        <div class="trait-item">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span data-fa>دقت و توجه عمیق به جزئیات</span>
                            <span data-en>Attention to Detail</span>
                        </div>
                        <div class="trait-item">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span data-fa>نظم و ساختارمندی اسناد</span>
                            <span data-en>Organization & Structure</span>
                        </div>
                        <div class="trait-item">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span data-fa>مسئولیت‌پذیری و پیگیری مستمر</span>
                            <span data-en>Accountability & Persistence</span>
                        </div>
                        <div class="trait-item">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span data-fa>یادگیری سریع سیستم‌های نوین</span>
                            <span data-en>Rapid Technical Learning</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="about-card reveal" style="transition-delay: 0.15s">
                <div>
                    <h3>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
                        <span data-fa>هدف شغلی و چشم‌انداز</span>
                        <span data-en>Career Objective & Vision</span>
                    </h3>
                    <p data-fa>
                        علاقه‌مند به همکاری موثر با مجموعه‌ها و شرکت‌های حرفه‌ای و پیشرو در حوزه حسابداری، مالی و بازرگانی، با هدف ارتقای تجارب عملیاتی، بهینه‌سازی سیستم‌های حسابداری، کنترل فرآیندهای انبارداری و تنخواه‌گردان، و ایجاد مسیری بلندمدت، متعهدانه و ارزش‌آفرین در حوزه مالی و مدیریت اقتصادی.
                    </p>
                    <p data-en>
                        Seeking to collaborate with forward-thinking organizations and enterprises in accounting, finance, and commerce. Dedicated to advancing practical expertise, streamlining bookkeeping & inventory workflows, managing petty cash with utmost transparency, and building a rewarding long-term career path in financial management.
                    </p>
                </div>
                <div style="background: var(--bg-card-subtle); border: 1px solid var(--silver-border); padding: 22px; border-radius: var(--radius-md);">
                    <div style="display: flex; gap: 14px; align-items: flex-start;">
                        <div style="color: var(--crimson-bright); font-size: 1.8rem; line-height: 1;">“</div>
                        <p style="margin: 0; font-size: 0.95rem; color: var(--text-secondary); font-style: italic;" data-fa>
                            حسابداری تنها ثبت اعداد نیست؛ بلکه زبان گویای شفافیت، سلامت و پایداری هر کسب‌وکار موفق است.
                        </p>
                        <p style="margin: 0; font-size: 0.95rem; color: var(--text-secondary); font-style: italic;" data-en>
                            Accounting is not merely recording numbers; it is the vital language of transparency, stability, and growth for every successful business.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <div class="section-divider"><i></i></div>

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
                            <div class="timeline-role" data-fa>حسابدار مالی</div>
                            <div class="timeline-role" data-en>Financial Accountant</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
                                <span data-fa>شرکت زمان‌نما پویش مهراد</span>
                                <span data-en>Zaman Nama Pooyesh Mehrad Co.</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>شهریور ۱۴۰۵ — آبان ۱۴۰۵</span>
                        <span class="timeline-date" data-en>Aug 2026 — Oct 2026</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        مدیریت حسابداری مالی، ثبت اسناد دریافت و پرداخت، نظارت بر سلامت رویدادهای مالی و گزارش‌گیری ادواری برای مدیریت.
                    </p>
                    <p class="timeline-desc" data-en>
                        Financial accounting management, processing ledger entries, supervising receivables/payables, and preparing periodic reports.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>ثبت، کنترل و بایگانی اسناد مالی روزانه و نظارت بر تطابق فاکتورها</li>
                        <li data-en>Daily bookkeeping, verifying transactional records, and maintaining financial document archives</li>
                        <li data-fa>انجام مغایرت‌گیری بانکی و پیگیری مطالبات و بدهی‌های تجاری</li>
                        <li data-en>Performing bank reconciliations and monitoring customer & vendor balances</li>
                        <li data-fa>ساماندهی تنخواه‌گردان و ثبت هزینه‌های اداری و اجرایی</li>
                        <li data-en>Administering petty cash funds and auditing departmental operating expenditures</li>
                    </ul>
                </div>
            </div>

            <!-- 2. رویال دیجی و دی پی کامپیوتر -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>حسابدار و مسئول کنترل موجودی و انبارداری</div>
                            <div class="timeline-role" data-en>Accountant & Inventory Controller</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                                <span data-fa>فروشگاه‌های اینترنتی رویال دیجی و دی‌پی کامپیوتر</span>
                                <span data-en>RoyalDigi & DP Computer E-Commerce</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>تیر ۱۴۰۵ — شهریور ۱۴۰۵</span>
                        <span data-en class="timeline-date">Jun 2026 — Aug 2026</span>
                    </div>

                    <div class="timeline-links">
                        <a href="https://royaldigi.ir/" target="_blank" rel="noopener noreferrer" class="website-link">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                            royaldigi.ir
                        </a>
                        <a href="https://dpcomputer.ir/" target="_blank" rel="noopener noreferrer" class="website-link">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                            dpcomputer.ir
                        </a>
                    </div>

                    <p class="timeline-desc" data-fa>
                        حسابداری فروشگاهی و انبارداری دو پلتفرم معتبر فروش کالای دیجیتال و قطعات سخت‌افزاری، کنترل ورود و خروج اقلام، قیمت‌گذاری و تطبیق انبار فیزیکی با سیستم.
                    </p>
                    <p class="timeline-desc" data-en>
                        Commercial retail & inventory accounting for premier digital product and IT hardware e-commerce stores, tracking inbound/outbound stocks, and reconciling physical inventory with digital systems.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>ثبت فاکتورهای خرید و فروش و کنترل حساب درگاه‌های پرداخت اینترنتی</li>
                        <li data-en>Recording purchase/sales invoices and auditing online payment gateway settlements</li>
                        <li data-fa>انبارگردانی دوره‌ای، بررسی کسری و اضافات انبار و تطبیق با کاردکس کالا</li>
                        <li data-en>Conducting periodic stocktakes, identifying inventory variances, and managing stock ledger cards</li>
                        <li data-fa>ثبت دریافت‌ها و پرداخت‌های تأمین‌کنندگان کالا و مشتریان آنلاین</li>
                        <li data-en>Managing accounts payable/receivable with equipment suppliers and end customers</li>
                    </ul>
                </div>
            </div>

            <!-- 3. شرکت گردشگری سرزمین اساطیری -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>حسابدار</div>
                            <div class="timeline-role" data-en>Accountant</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                                <span data-fa>شرکت خدمات مسافرتی و گردشگری سرزمین اساطیری</span>
                                <span data-en>Sarzamin Asatiri Tourism & Travel Agency</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>مرداد ۱۴۰۴ — آبان ۱۴۰۴</span>
                        <span class="timeline-date" data-en>Jul 2025 — Oct 2025</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        حسابداری مالی و عملیاتی تورهای داخلی و خارجی، صدور اسناد تسویه‌حساب با آژانس‌های همکار و مدیریت هزینه‌های ارزی/ریالی.
                    </p>
                    <p class="timeline-desc" data-en>
                        Financial accounting for travel and tour operations, vendor reconciliations with airlines & hotels, and operational expense control.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>ثبت اسناد درآمدی و هزینه‌ای تورها، بلیت‌ها و هتل‌ها</li>
                        <li data-en>Bookkeeping tour revenues, ticketing transactions, and accommodation costs</li>
                        <li data-fa>مدیریت تنخواه هزینه‌های عملیاتی تور و کنترل اسناد مثبته</li>
                        <li data-en>Supervising tour operational petty cash funds and validating expense receipts</li>
                    </ul>
                </div>
            </div>

            <!-- 4. شرکت همایشگران سام -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>ادمین و هماهنگ‌کننده اجرایی</div>
                            <div class="timeline-role" data-en>Administrative & Operations Coordinator</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                                <span data-fa>شرکت همایشگران سام</span>
                                <span data-en>Hamayeshgaran Sam Co.</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>اردیبهشت ۱۴۰۴ — آذر ۱۴۰۴</span>
                        <span class="timeline-date" data-en>Apr 2025 — Nov 2025</span>
                    </div>
                    <p class="timeline-desc" data-fa>
                        مدیریت اداری، هماهنگی امور برگزاری همایش‌ها و رویدادهای تخصصی، بایگانی قراردادها و ارتباط با کارفرمایان.
                    </p>
                    <p class="timeline-desc" data-en>
                        Administrative management, coordinating convention logistics, organizing vendor agreements, and handling communications.
                    </p>
                    <ul class="timeline-tasks">
                        <li data-fa>ساماندهی مکاتبات و پرونده‌های مالی و اداری رویدادها</li>
                        <li data-en>Structuring event administrative records, invoicing, and communications</li>
                        <li data-fa>پشتیبانی اجرایی، پاسخگویی به مراجعین و مدیریت جریان اسناد</li>
                        <li data-en>Operations support, client follow-up, and digital documentation control</li>
                    </ul>
                </div>
            </div>

            <!-- 5. مهدکودک ققنوس -->
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <div class="timeline-card">
                    <div class="timeline-top">
                        <div>
                            <div class="timeline-role" data-fa>کمک‌حسابدار و مسئول تنخواه‌گردان</div>
                            <div class="timeline-role" data-en>Junior Accountant & Petty Cash Officer</div>
                            <div class="timeline-company">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                                <span data-fa>مجموعه آموزشی و مهدکودک ققنوس</span>
                                <span data-en>Ghoghnous Educational Complex</span>
                            </div>
                        </div>
                        <span class="timeline-date" data-fa>خرداد ۱۴۰۴ — آذر ۱۴۰۴</span>
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

    <div class="section-divider"><i></i></div>

    <!-- Skills & Tools Section -->
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
                            <span class="level" data-fa>مسلط (۸۸٪)</span>
                            <span class="level" data-en>Proficient (88%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 88%;"></div></div>
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
                            <span class="level" data-fa>تخصصی (۹۴٪)</span>
                            <span class="level" data-en>Expert (94%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 94%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>مدیریت و کنترل تنخواه‌گردان</span>
                            <span class="name" data-en>Petty Cash Oversight</span>
                            <span class="level" data-fa>تخصصی (۹۲٪)</span>
                            <span class="level" data-en>Expert (92%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 92%;"></div></div>
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
                            <span class="level" data-fa>مسلط (۸۸٪)</span>
                            <span class="level" data-en>Proficient (88%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 88%;"></div></div>
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
                            <span class="level" data-fa>پیشرفته (۹۲٪)</span>
                            <span class="level" data-en>Advanced (92%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 92%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>مهارت‌های هفتگانه ICDL</span>
                            <span class="name" data-en>ICDL Comprehensive</span>
                            <span class="level" data-fa>مسلط (۹۰٪)</span>
                            <span class="level" data-en>Proficient (90%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 90%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>امور مالیاتی و اظهارنامه (مقدماتی)</span>
                            <span class="name" data-en>Tax Basics & Declarations</span>
                            <span class="level" data-fa>خوب (۷۵٪)</span>
                            <span class="level" data-en>Competent (75%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 75%;"></div></div>
                    </div>

                    <div class="skill-bar-item">
                        <div class="skill-info">
                            <span class="name" data-fa>یادگیری سریع ابزارهای دیجیتال</span>
                            <span class="name" data-en>Rapid Software Adoption</span>
                            <span class="level" data-fa>عالی (۹۸٪)</span>
                            <span class="level" data-en>Excellent (98%)</span>
                        </div>
                        <div class="skill-track"><div class="skill-fill" style="width: 98%;"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Language Proficiency Box -->
        <div class="lang-section reveal">
            <div class="lang-grid">
                <div class="lang-meta">
                    <span class="lang-tag" data-fa>ارزیابی زبان بین‌المللی</span>
                    <span class="lang-tag" data-en>Language Proficiency</span>
                    <h3 style="margin-top: 14px;" data-fa>زبان انگلیسی</h3>
                    <h3 style="margin-top: 14px;" data-en>English Language</h3>
                    <p data-fa>
                        دارای بیش از ۱۴ سال سابقه آموزش پیوسته و مطالعه منابع تخصصی زبان انگلیسی. تسلط کامل بر مکاتبات، مطالعه متون و گزارش‌های مالی بین‌المللی.
                    </p>
                    <p data-en>
                        Over 14 years of dedicated English language study and immersion. Highly proficient in professional correspondence, reading technical finance reports, and documentation.
                    </p>
                    <div style="font-size: 0.9rem; color: var(--text-muted);">
                        <strong style="color: var(--text-main);" data-fa>مجموع ارزیابی:</strong>
                        <strong style="color: var(--text-main);" data-en>Overall Rating:</strong>
                        <span data-fa> بسیار خوب (Upper-Intermediate)</span>
                        <span data-en> Very Good (Upper-Intermediate)</span>
                    </div>
                </div>

                <div class="lang-skills-grid">
                    <!-- Listening -->
                    <div class="lang-skill-card">
                        <div class="lang-skill-header">
                            <span class="title" data-fa>مهارت شنیداری (Listening)</span>
                            <span class="title" data-en>Listening Comprehension</span>
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
                            <span class="title" data-fa>خواندن و درک مطلب (Reading)</span>
                            <span class="title" data-en>Reading & Comprehension</span>
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
                            <span class="title" data-fa>نگارش و مکاتبه (Writing)</span>
                            <span class="title" data-en>Professional Writing</span>
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
                            <span class="title" data-fa>مکالمه و گفتاری (Speaking)</span>
                            <span class="title" data-en>Spoken Communication</span>
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
        </div>
    </section>

    <div class="section-divider"><i></i></div>

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
            <!-- Academic Degree -->
            <div class="edu-card reveal">
                <div class="edu-icon-wrap">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
                </div>
                <div class="edu-info">
                    <span class="edu-badge" data-fa>در حال تحصیل — ترم پنجم</span>
                    <span class="edu-badge" data-en>In Progress — 5th Semester</span>
                    <h3 style="margin-top: 10px;" data-fa>کارشناسی حسابداری</h3>
                    <h3 style="margin-top: 10px;" data-en>B.Sc. in Accounting</h3>
                    <h4 data-fa>دانشگاه آزاد اسلامی، واحد تهران مرکزی (مجتمع سوهانک)</h4>
                    <h4 data-en>Islamic Azad University, Central Tehran Branch</h4>
                    <p data-fa>
                        فراگیری عمیق مبانی حسابداری مالی، حسابداری صنعتی، حسابرسی، قوانین مالیاتی، مدیریت مالی و اقتصاد کاربردی با انگیزه بالا برای ورود حرفه‌ای به بازار کار.
                    </p>
                    <p data-en>
                        Rigorous coursework in financial accounting, cost accounting, auditing, commercial tax law, and financial management.
                    </p>
                </div>
            </div>

            <!-- Professional Certifications -->
            <div class="edu-card reveal" style="transition-delay: 0.15s">
                <div class="edu-icon-wrap">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
                </div>
                <div class="edu-info">
                    <span class="edu-badge" data-fa>مدارک رسمی و معتبر</span>
                    <span class="edu-badge" data-en>Accredited Certifications</span>
                    <h3 style="margin-top: 10px;" data-fa>مدرک جامع حسابداری و سپیدار</h3>
                    <h3 style="margin-top: 10px;" data-en>Comprehensive Accounting & Sepidar</h3>
                    <h4 data-fa>مجتمع فنی تهران (MFT)</h4>
                    <h4 data-en>Tehran Technical Complex (MFT)</h4>
                    <p data-fa>
                        گواهینامه رسمی دوره جامع حسابداری، ثبت و کنترل دفاتر قانونی، تهیه صورت‌های مالی، مغایرت‌گیری و گواهینامه تخصصی کار با نرم‌افزار حسابداری سپیدار همکاران سیستم.
                    </p>
                    <p data-en>
                        Official certification in comprehensive accounting, general ledger entries, preparation of financial statements, and certified proficiency in Sepidar ERP software.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <div class="section-divider"><i></i></div>

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
            <!-- Contact Details -->
            <div class="contact-info-panel reveal">
                <h3 data-fa>اطلاعات مستقیم تماس</h3>
                <h3 data-en>Direct Contact Information</h3>
                <p data-fa>
                    خوشحال می‌شوم با مجموعه‌ها و کارفرمایان محترم جهت همکاری در موقعیت‌های حسابداری، کمک‌حسابداری و مدیریت مالی گفتگو داشته باشم.
                </p>
                <p data-en>
                    I welcome conversations with organizations, companies, and executives regarding accounting, financial analyst, or audit positions.
                </p>

                <div class="contact-list">
                    <!-- Phone -->
                    <a href="tel:09034443342" class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>تلفن تماس همراه</span>
                            <span class="label" data-en>Mobile Phone</span>
                            <span class="val">0903 444 3342</span>
                        </div>
                    </a>

                    <!-- Email -->
                    <a href="mailto:Parsa.kodari@gmail.com" class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>آدرس پست الکترونیکی</span>
                            <span class="label" data-en>Email Address</span>
                            <span class="val">Parsa.kodari@gmail.com</span>
                        </div>
                    </a>

                    <!-- Instagram -->
                    <a href="https://instagram.com/Parsa___kodari" target="_blank" rel="noopener noreferrer" class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>صفحه کاری اینستاگرام</span>
                            <span class="label" data-en>Business Instagram</span>
                            <span class="val">@Parsa___kodari</span>
                        </div>
                    </a>

                    <!-- Location -->
                    <div class="contact-item">
                        <div class="contact-item-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        </div>
                        <div class="contact-item-text">
                            <span class="label" data-fa>محل سکونت</span>
                            <span class="label" data-en>Location</span>
                            <span class="val" data-fa style="direction: rtl; text-align: right;">تهران، سعادت‌آباد</span>
                            <span class="val" data-en>Tehran, Sa'adat Abad</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Quick Direct Contact Form -->
            <div class="contact-form-panel reveal" style="transition-delay: 0.15s">
                <form id="contactForm">
                    <div class="form-group">
                        <label for="cName" data-fa>نام و نام خانوادگی / نام سازمان</label>
                        <label for="cName" data-en>Your Name / Organization</label>
                        <input type="text" class="form-control" id="cName" placeholder="مثال: علی محمدی / شرکت ..." required>
                    </div>

                    <div class="form-group">
                        <label for="cPhone" data-fa>شماره تماس همراه</label>
                        <label for="cPhone" data-en>Phone Number</label>
                        <input type="tel" class="form-control" id="cPhone" placeholder="09xxxxxxxxx" required>
                    </div>

                    <div class="form-group">
                        <label for="cMessage" data-fa>متن پیام یا شرح موقعیت شغلی</label>
                        <label for="cMessage" data-en>Message / Opportunity Details</label>
                        <textarea class="form-control" id="cMessage" placeholder="پیام خود را اینجا بنویسید..." required></textarea>
                    </div>

                    <button type="submit" class="btn btn-primary form-btn">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        <span data-fa>ارسال سریع پیامک به پارسا کدری</span>
                        <span data-en>Send Direct SMS</span>
                    </button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <svg width="56" height="34" viewBox="0 0 240 140" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <text x="15" y="106" font-family="'Playfair Display', Georgia, serif" font-size="110" font-weight="700" fill="#730f23">P</text>
                        <text x="74" y="106" font-family="'Playfair Display', Georgia, serif" font-size="110" font-weight="700" fill="#6e6868">K</text>
                        <line x1="195" y1="22" x2="195" y2="118" stroke="#8a8585" stroke-width="5" stroke-linecap="round" />
                    </svg>
                    <div>
                        <h4 style="color: var(--text-main); font-weight: 700;" data-fa>پارسا کدری</h4>
                        <h4 style="color: var(--text-main); font-weight: 700;" data-en>Parsa Kodari</h4>
                        <p style="font-size: 0.8rem; color: var(--text-muted);" data-fa>حسابدار و کارشناس امور مالی | دانشجوی کارشناسی حسابداری</p>
                        <p style="font-size: 0.8rem; color: var(--text-muted);" data-en>Accountant & Financial Specialist</p>
                    </div>
                </div>

                <div class="footer-socials">
                    <a href="tel:09034443342" class="social-link" title="تماس تلفنی" aria-label="Phone">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                    </a>
                    <a href="mailto:Parsa.kodari@gmail.com" class="social-link" title="ارسال ایمیل" aria-label="Email">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    </a>
                    <a href="https://instagram.com/Parsa___kodari" target="_blank" rel="noopener noreferrer" class="social-link" title="اینستاگرام" aria-label="Instagram">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                </div>
            </div>

            <div class="footer-bottom">
                <p>© ۲۰۲۶ پارسا کدری — وب‌سایت و پورتفولیو رسمی | <a href="https://parsakodari.ir/" style="color: var(--crimson-bright);">parsakodari.ir</a></p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script>
        // --- Language Toggle System (FA / EN) ---
        function setLanguage(lang) {{
            document.documentElement.setAttribute('data-language', lang);
            document.documentElement.dir = (lang === 'fa') ? 'rtl' : 'ltr';
            document.documentElement.lang = lang;
            
            document.querySelectorAll('.lang-btn').forEach(btn => {{
                btn.classList.toggle('active', btn.dataset.lang === lang);
            }});
            
            // Update title
            if (lang === 'en') {{
                document.title = "Parsa Kodari | Accountant & Financial Specialist | Portfolio";
            }} else {{
                document.title = "پارسا کدری | حسابدار و کارشناس امور مالی | Parsa Kodari";
            }}
        }}

        document.querySelectorAll('.lang-btn').forEach(btn => {{
            btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
        }});

        // --- Mobile Navigation Menu ---
        const hamburger = document.querySelector('.hamburger');
        const navLinks = document.querySelector('.nav-links');

        hamburger.addEventListener('click', () => {{
            navLinks.classList.toggle('active');
        }});

        document.querySelectorAll('.nav-links a').forEach(link => {{
            link.addEventListener('click', () => {{
                navLinks.classList.remove('active');
            }});
        }});

        // --- Scroll Reveal Animations ---
        const observerOptions = {{
            threshold: 0.12,
            rootMargin: "0px 0px -40px 0px"
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

print('Successfully generated index.html with Silver-Gray and Crimson theme!')
