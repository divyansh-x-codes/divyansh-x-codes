#!/usr/bin/env python3
import base64
import os
import zipfile

WORKSPACE = "/Users/Apple/Desktop/github"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")

def get_base64_image(filename):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "rb") as f:
        data = f.read()
    return f"data:image/png;base64,{base64.b64encode(data).decode('utf-8')}"

id_b64 = get_base64_image("id_opt.png")
pointing_b64 = get_base64_image("right_pointing_opt.png")
profiles_b64 = get_base64_image("profiles.png")
stack_b64 = get_base64_image("stack.png")

# -------------------------------------------------------------
# 1. HERO.SVG
# -------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 390" width="880" height="390" fill="none">
  <defs>
    <style>
      @keyframes hero-pulse {{
        0%, 100% {{ opacity: 0.25; transform: scale(1); }}
        50% {{ opacity: 0.55; transform: scale(1.06); }}
      }}
      @keyframes hero-dot-glow {{
        0%, 100% {{ opacity: 0.4; }}
        50% {{ opacity: 1; }}
      }}
      @keyframes hero-name-rise {{
        0% {{ transform: translateY(40px); opacity: 0; }}
        100% {{ transform: translateY(0); opacity: 1; }}
      }}
      @keyframes hero-role-1 {{
        0%, 20% {{ opacity: 1; transform: translateY(0); }}
        23%, 97% {{ opacity: 0; transform: translateY(12px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes hero-role-2 {{
        0%, 22% {{ opacity: 0; transform: translateY(-12px); }}
        25%, 45% {{ opacity: 1; transform: translateY(0); }}
        48%, 100% {{ opacity: 0; transform: translateY(12px); }}
      }}
      @keyframes hero-role-3 {{
        0%, 47% {{ opacity: 0; transform: translateY(-12px); }}
        50%, 70% {{ opacity: 1; transform: translateY(0); }}
        73%, 100% {{ opacity: 0; transform: translateY(12px); }}
      }}
      @keyframes hero-role-4 {{
        0%, 72% {{ opacity: 0; transform: translateY(-12px); }}
        75%, 95% {{ opacity: 1; transform: translateY(0); }}
        98%, 100% {{ opacity: 0; transform: translateY(12px); }}
      }}
      @keyframes hero-float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-6px); }}
      }}
      .hero-font {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      }}
      .hero-mono {{
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
      }}
      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
      }}
    </style>

    <linearGradient id="hero-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060a14"/>
      <stop offset="50%" stop-color="#091122"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>

    <linearGradient id="hero-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#1e293b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.85"/>
    </linearGradient>

    <linearGradient id="hero-text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#f0f6fc"/>
      <stop offset="100%" stop-color="#60a5fa"/>
    </linearGradient>

    <radialGradient id="hero-blue-glow" cx="80%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="hero-red-glow" cx="20%" cy="80%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>

    <pattern id="hero-dot-pattern" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#247bff" fill-opacity="0.14"/>
    </pattern>

    <clipPath id="hero-card-clip">
      <rect x="0" y="0" width="880" height="390" rx="16"/>
    </clipPath>

    <clipPath id="hero-name-clip">
      <rect x="0" y="0" width="530" height="55"/>
    </clipPath>

    <clipPath id="hero-avatar-clip">
      <rect x="0" y="0" width="255" height="312" rx="18"/>
    </clipPath>
  </defs>

  <!-- Background Card -->
  <g clip-path="url(#hero-card-clip)">
    <rect x="0" y="0" width="880" height="390" fill="url(#hero-bg-grad)"/>
    <rect x="0" y="0" width="880" height="390" fill="url(#hero-dot-pattern)"/>
    
    <circle cx="730" cy="140" r="230" fill="url(#hero-blue-glow)" style="animation: hero-pulse 8s ease-in-out infinite;"/>
    <circle cx="140" cy="310" r="180" fill="url(#hero-red-glow)" style="animation: hero-pulse 6s ease-in-out infinite alternate;"/>

    <!-- Left Content Column -->
    <g transform="translate(42, 38)">
      <!-- Status Badge -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="250" height="26" rx="13" fill="#0d1829" stroke="#247bff" stroke-opacity="0.4" stroke-width="1"/>
        <circle cx="13" cy="13" r="3.5" fill="#00ff88" style="animation: hero-dot-glow 2s infinite ease-in-out;"/>
        <circle cx="13" cy="13" r="7" fill="#00ff88" fill-opacity="0.25" style="animation: hero-dot-glow 2s infinite ease-in-out;"/>
        <text x="26" y="17" fill="#58a6ff" class="hero-mono" font-size="10.5" font-weight="600" letter-spacing="1">SYS.INIT // AI &amp; ML SPECIALIST</text>
      </g>

      <!-- Subtitle Greeting -->
      <g transform="translate(0, 44)">
        <text x="0" y="16" fill="#8b949e" class="hero-mono" font-size="13" font-weight="500" letter-spacing="2">
          HEY THERE, WORLD! I AM
        </text>
      </g>

      <!-- Rising Mask Name Reveal -->
      <g transform="translate(0, 70)" clip-path="url(#hero-name-clip)">
        <g style="animation: hero-name-rise 0.9s cubic-bezier(0.16, 1, 0.3, 1) forwards;">
          <text x="0" y="38" fill="url(#hero-text-grad)" class="hero-font" font-size="36" font-weight="900" letter-spacing="-0.5">
            DIVYANSH CHAUDHARY
          </text>
        </g>
      </g>

      <!-- Cycling Dynamic Roles -->
      <g transform="translate(0, 136)">
        <text x="0" y="20" fill="#ff354f" class="hero-mono" font-size="18" font-weight="800">&gt;</text>
        
        <!-- Role 1 -->
        <g transform="translate(22, 0)" style="animation: hero-role-1 12s infinite cubic-bezier(0.4, 0, 0.2, 1);">
          <text x="0" y="20" fill="#f0f6fc" class="hero-font" font-size="18.5" font-weight="700">AI / ML Student &amp; Researcher</text>
        </g>
        <!-- Role 2 -->
        <g transform="translate(22, 0)" style="animation: hero-role-2 12s infinite cubic-bezier(0.4, 0, 0.2, 1);">
          <text x="0" y="20" fill="#58a6ff" class="hero-font" font-size="18.5" font-weight="700">Machine Learning Developer</text>
        </g>
        <!-- Role 3 -->
        <g transform="translate(22, 0)" style="animation: hero-role-3 12s infinite cubic-bezier(0.4, 0, 0.2, 1);">
          <text x="0" y="20" fill="#00ff88" class="hero-font" font-size="18.5" font-weight="700">Applied AI &amp; Neural Engineer</text>
        </g>
        <!-- Role 4 -->
        <g transform="translate(22, 0)" style="animation: hero-role-4 12s infinite cubic-bezier(0.4, 0, 0.2, 1);">
          <text x="0" y="20" fill="#ff7b72" class="hero-font" font-size="18.5" font-weight="700">Full-Stack Platform Developer</text>
        </g>
      </g>

      <!-- One-line Pitch -->
      <g transform="translate(0, 178)">
        <text x="0" y="16" fill="#94a3b8" class="hero-font" font-size="13.5" font-weight="400">
          Building intelligent AI systems, neural models &amp; high-scale platforms.
        </text>
      </g>

      <!-- Meta Pill Badges -->
      <g transform="translate(0, 230)">
        <rect x="0" y="0" width="205" height="34" rx="8" fill="#0b1322" stroke="#1f2d48" stroke-width="1"/>
        <path d="M16 11C13.24 11 11 13.24 11 16C11 19.75 16 25 16 25C16 25 21 19.75 21 16C21 13.24 18.76 11 16 11ZM16 17.5C15.17 17.5 14.5 16.83 14.5 16C14.5 15.17 15.17 14.5 16 14.5C16.83 14.5 17.5 15.17 17.5 16C17.5 16.83 16.83 17.5 16 17.5Z" fill="#ff354f"/>
        <text x="32" y="22" fill="#c9d1d9" class="hero-font" font-size="11.5" font-weight="500">Sonipat, Haryana, India</text>

        <g transform="translate(217, 0)">
          <rect x="0" y="0" width="225" height="34" rx="8" fill="#0b1322" stroke="#1f2d48" stroke-width="1"/>
          <path d="M12 11L19 15L12 19L5 15L12 11ZM5 17.5L12 21.5L19 17.5M5 20.5L12 24.5L19 20.5" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="32" y="22" fill="#c9d1d9" class="hero-font" font-size="11.5" font-weight="500">Building Ryth (200+ Users)</text>
        </g>
      </g>
    </g>

    <!-- Right Column: Stylized Portrait Card -->
    <g transform="translate(580, 34)">
      <rect x="0" y="0" width="260" height="320" rx="20" fill="none" stroke="url(#hero-border-grad)" stroke-width="1.8" style="filter: drop-shadow(0px 8px 24px rgba(36,123,255,0.22));"/>
      
      <g style="animation: hero-float 5s ease-in-out infinite;">
        <rect x="3" y="3" width="254" height="314" rx="17" fill="#0b1322"/>
        
        <g clip-path="url(#hero-avatar-clip)" transform="translate(2, 2)">
          <image href="{id_b64}" x="-15" y="-10" width="285" height="330" preserveAspectRatio="xMidYMid slice"/>
        </g>

        <rect x="3" y="220" width="254" height="94" rx="17" fill="url(#hero-bg-grad)" fill-opacity="0.88"/>

        <g transform="translate(16, 266)">
          <rect x="0" y="0" width="226" height="36" rx="8" fill="#070b16" fill-opacity="0.9" stroke="#247bff" stroke-opacity="0.5" stroke-width="1"/>
          <circle cx="14" cy="18" r="3.5" fill="#247bff"/>
          <text x="26" y="22" fill="#ffffff" class="hero-font" font-size="12" font-weight="700">DIVYANSH.ID</text>
          <text x="140" y="22" fill="#58a6ff" class="hero-mono" font-size="10.5" font-weight="600">VERIFIED // 01</text>
        </g>

        <path d="M12 24V12H24" stroke="#247bff" stroke-width="2" stroke-linecap="round"/>
        <path d="M248 24V12H236" stroke="#ff354f" stroke-width="2" stroke-linecap="round"/>
      </g>
    </g>

    <!-- Outer Frame Stroke -->
    <rect x="1" y="1" width="878" height="388" rx="15" fill="none" stroke="url(#hero-border-grad)" stroke-width="1.5"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. ABOUT-LIFE.SVG - ZERO OVERLAPS, FLAWLESS CAROUSEL ALIGNMENT
# -------------------------------------------------------------
about_life_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 370" width="880" height="370" fill="none">
  <defs>
    <style>
      .about-font {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      }}
      .about-mono {{
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
      }}

      @keyframes slide-anim-1 {{
        0%, 28% {{ opacity: 1; visibility: visible; }}
        33.3%, 94.7% {{ opacity: 0; visibility: hidden; }}
        100% {{ opacity: 1; visibility: visible; }}
      }}

      @keyframes slide-anim-2 {{
        0%, 28% {{ opacity: 0; visibility: hidden; }}
        33.3%, 61.3% {{ opacity: 1; visibility: visible; }}
        66.6%, 100% {{ opacity: 0; visibility: hidden; }}
      }}

      @keyframes slide-anim-3 {{
        0%, 61.3% {{ opacity: 0; visibility: hidden; }}
        66.6%, 94.7% {{ opacity: 1; visibility: visible; }}
        100% {{ opacity: 0; visibility: hidden; }}
      }}

      .carousel-slide-1 {{
        animation: slide-anim-1 12s infinite ease-in-out;
      }}
      .carousel-slide-2 {{
        animation: slide-anim-2 12s infinite ease-in-out;
      }}
      .carousel-slide-3 {{
        animation: slide-anim-3 12s infinite ease-in-out;
      }}

      @keyframes border-breathe {{
        0%, 100% {{ stroke-opacity: 0.5; }}
        50% {{ stroke-opacity: 0.85; }}
      }}

      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
        .carousel-slide-1 {{ opacity: 1 !important; visibility: visible !important; }}
        .carousel-slide-2 {{ display: none !important; }}
        .carousel-slide-3 {{ display: none !important; }}
      }}
    </style>

    <linearGradient id="about-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050813"/>
      <stop offset="50%" stop-color="#081022"/>
      <stop offset="100%" stop-color="#040711"/>
    </linearGradient>

    <linearGradient id="about-card-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0c1527"/>
      <stop offset="100%" stop-color="#080e1b"/>
    </linearGradient>

    <linearGradient id="about-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.85"/>
      <stop offset="50%" stop-color="#1e293b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.85"/>
    </linearGradient>

    <pattern id="about-grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#247bff" stroke-opacity="0.04" stroke-width="1"/>
    </pattern>

    <clipPath id="about-main-clip">
      <rect x="0" y="0" width="880" height="370" rx="16"/>
    </clipPath>
  </defs>

  <g clip-path="url(#about-main-clip)">
    <!-- Main Background -->
    <rect width="880" height="370" fill="url(#about-bg-grad)"/>
    <rect width="880" height="370" fill="url(#about-grid)"/>

    <!-- ==================== HEADER ==================== -->
    <g transform="translate(42, 24)">
      <!-- Section Pill Badge -->
      <rect x="0" y="0" width="220" height="28" rx="7" fill="#0c182b" stroke="#247bff" stroke-opacity="0.5" stroke-width="1.2"/>
      <circle cx="14" cy="14" r="3.5" fill="#247bff"/>
      <text x="26" y="18" fill="#58a6ff" class="about-mono" font-size="11" font-weight="800" letter-spacing="1">02 // CAPABILITIES &amp; LIFE</text>
      
      <!-- Subtitle -->
      <text x="240" y="18" fill="#94a3b8" class="about-font" font-size="13" font-weight="500">What drives my technical craftsmanship and daily curiosity</text>
    </g>

    <!-- ==================== LEFT CARD: CORE CAPABILITIES ==================== -->
    <g transform="translate(42, 66)">
      <!-- Card Container -->
      <rect width="386" height="276" rx="14" fill="url(#about-card-grad)" stroke="#1a2744" stroke-width="1.2"/>
      
      <!-- Card Header -->
      <text x="20" y="28" fill="#ffffff" class="about-font" font-size="14.5" font-weight="800" letter-spacing="0.5">CORE CAPABILITIES</text>
      <rect x="318" y="14" width="48" height="20" rx="4" fill="#0d2238" stroke="#247bff" stroke-opacity="0.4" stroke-width="0.8"/>
      <text x="342" y="28" text-anchor="middle" fill="#60a5fa" class="about-mono" font-size="9" font-weight="700">SPEC</text>
      <line x1="20" y1="44" x2="366" y2="44" stroke="#16233b" stroke-width="1"/>

      <!-- Capability 1: AI / ML -->
      <g transform="translate(20, 60)">
        <rect x="0" y="0" width="38" height="38" rx="8" fill="#0d2238" stroke="#247bff" stroke-opacity="0.5" stroke-width="1"/>
        <path d="M13 19C13 15.7 15.7 13 19 13C22.3 13 25 15.7 25 19C25 22.3 22.3 25 19 25" stroke="#58a6ff" stroke-width="2" stroke-linecap="round"/>
        <circle cx="19" cy="19" r="2.5" fill="#00ff88"/>
        <text x="50" y="16" fill="#ffffff" class="about-font" font-size="13" font-weight="700">Applied AI &amp; Machine Learning</text>
        <text x="50" y="32" fill="#94a3b8" class="about-font" font-size="10.5">TensorFlow, Scikit-learn, Neural Nets &amp; Vision</text>
      </g>

      <!-- Capability 2: Full-Stack -->
      <g transform="translate(20, 126)">
        <rect x="0" y="0" width="38" height="38" rx="8" fill="#261318" stroke="#ff354f" stroke-opacity="0.5" stroke-width="1"/>
        <path d="M12 15L19 11L26 15L19 19L12 15ZM12 21L19 25L26 21" stroke="#ff7b72" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="50" y="16" fill="#ffffff" class="about-font" font-size="13" font-weight="700">Full-Stack Architecture</text>
        <text x="50" y="32" fill="#94a3b8" class="about-font" font-size="10.5">React, Node.js, Express, REST APIs &amp; SQL</text>
      </g>

      <!-- Capability 3: Systems & C++ -->
      <g transform="translate(20, 192)">
        <rect x="0" y="0" width="38" height="38" rx="8" fill="#072418" stroke="#00ff88" stroke-opacity="0.5" stroke-width="1"/>
        <path d="M19 12V26M12 19H26" stroke="#00ff88" stroke-width="2" stroke-linecap="round"/>
        <text x="50" y="16" fill="#ffffff" class="about-font" font-size="13" font-weight="700">Systems, Algorithms &amp; C++</text>
        <text x="50" y="32" fill="#94a3b8" class="about-font" font-size="10.5">Low-level efficiency, Clean Code &amp; Git ELT</text>
      </g>
    </g>

    <!-- ==================== RIGHT CARD: PASSIONS & ETHOS (CAROUSEL) ==================== -->
    <g transform="translate(452, 66)">
      <!-- Card Container -->
      <rect width="386" height="276" rx="14" fill="url(#about-card-grad)" stroke="#1a2744" stroke-width="1.2"/>
      
      <!-- Card Header -->
      <text x="20" y="28" fill="#ffffff" class="about-font" font-size="14.5" font-weight="800" letter-spacing="0.5">INTERESTS &amp; PASSIONS</text>
      <rect x="314" y="14" width="52" height="20" rx="4" fill="#2a1217" stroke="#ff354f" stroke-opacity="0.4" stroke-width="0.8"/>
      <text x="340" y="28" text-anchor="middle" fill="#ff7b72" class="about-mono" font-size="9" font-weight="700">ETHOS</text>
      <line x1="20" y1="44" x2="366" y2="44" stroke="#16233b" stroke-width="1"/>

      <!-- Slides Container (Static translate position) -->
      <g transform="translate(20, 60)">
        <!-- SLIDE 1: ADRENALINE / RACING -->
        <g class="carousel-slide-1" style="opacity: 1;">
          <!-- Badge & Progress Indicators -->
          <rect x="0" y="0" width="118" height="22" rx="4" fill="#2a1217" stroke="#ff354f" stroke-opacity="0.5" stroke-width="0.8"/>
          <text x="10" y="15" fill="#ff7b72" class="about-mono" font-size="9.5" font-weight="700" letter-spacing="1">01 / ADRENALINE</text>
          
          <rect x="242" y="9" width="30" height="4" rx="2" fill="#ff354f"/>
          <rect x="278" y="9" width="30" height="4" rx="2" fill="#1e293b"/>
          <rect x="314" y="9" width="30" height="4" rx="2" fill="#1e293b"/>

          <!-- Title -->
          <text x="0" y="52" fill="#ffffff" class="about-font" font-size="18" font-weight="800" letter-spacing="0.2">Car Racing &amp; Dynamics</text>

          <!-- Description -->
          <text x="0" y="78" fill="#94a3b8" class="about-font" font-size="12">The thrill of high-speed aerodynamics, apex precision, and</text>
          <text x="0" y="98" fill="#94a3b8" class="about-font" font-size="12">high-stakes split-second decision making under pressure.</text>

          <!-- Ethos Box -->
          <g transform="translate(0, 126)">
            <rect x="0" y="0" width="346" height="42" rx="8" fill="#180e12" stroke="#ff354f" stroke-opacity="0.35" stroke-width="1"/>
            <text x="16" y="26" fill="#ff7b72" class="about-mono" font-size="10.5" font-weight="700" letter-spacing="0.5">ETHOS: Speed · Telemetry · Peak Precision</text>
          </g>
        </g>

        <!-- SLIDE 2: VENTURE / ENTREPRENEURSHIP -->
        <g class="carousel-slide-2" style="opacity: 0;">
          <!-- Badge & Progress Indicators -->
          <rect x="0" y="0" width="102" height="22" rx="4" fill="#072418" stroke="#00ff88" stroke-opacity="0.5" stroke-width="0.8"/>
          <text x="10" y="15" fill="#00ff88" class="about-mono" font-size="9.5" font-weight="700" letter-spacing="1">02 / VENTURE</text>
          
          <rect x="242" y="9" width="30" height="4" rx="2" fill="#1e293b"/>
          <rect x="278" y="9" width="30" height="4" rx="2" fill="#00ff88"/>
          <rect x="314" y="9" width="30" height="4" rx="2" fill="#1e293b"/>

          <!-- Title -->
          <text x="0" y="52" fill="#ffffff" class="about-font" font-size="18" font-weight="800" letter-spacing="0.2">Entrepreneurship &amp; Building</text>

          <!-- Description -->
          <text x="0" y="78" fill="#94a3b8" class="about-font" font-size="12">Founder of Ryth (200+ users). Engineering growth platforms,</text>
          <text x="0" y="98" fill="#94a3b8" class="about-font" font-size="12">product architecture, and high-velocity creator ecosystems.</text>

          <!-- Ethos Box -->
          <g transform="translate(0, 126)">
            <rect x="0" y="0" width="346" height="42" rx="8" fill="#091d14" stroke="#00ff88" stroke-opacity="0.35" stroke-width="1"/>
            <text x="16" y="26" fill="#00ff88" class="about-mono" font-size="10.5" font-weight="700" letter-spacing="0.5">ETHOS: Vision · Scale · Relentless Execution</text>
          </g>
        </g>

        <!-- SLIDE 3: RESEARCH / DEEP TECH -->
        <g class="carousel-slide-3" style="opacity: 0;">
          <!-- Badge & Progress Indicators -->
          <rect x="0" y="0" width="112" height="22" rx="4" fill="#0d2238" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="0.8"/>
          <text x="10" y="15" fill="#38bdf8" class="about-mono" font-size="9.5" font-weight="700" letter-spacing="1">03 / RESEARCH</text>
          
          <rect x="242" y="9" width="30" height="4" rx="2" fill="#1e293b"/>
          <rect x="278" y="9" width="30" height="4" rx="2" fill="#1e293b"/>
          <rect x="314" y="9" width="30" height="4" rx="2" fill="#38bdf8"/>

          <!-- Title -->
          <text x="0" y="52" fill="#ffffff" class="about-font" font-size="18" font-weight="800" letter-spacing="0.2">Deep Tech &amp; AI Research</text>

          <!-- Description -->
          <text x="0" y="78" fill="#94a3b8" class="about-font" font-size="12">Exploring neural intelligence, autonomous agent workflows,</text>
          <text x="0" y="98" fill="#94a3b8" class="about-font" font-size="12">and scalable distributed computation architectures.</text>

          <!-- Ethos Box -->
          <g transform="translate(0, 126)">
            <rect x="0" y="0" width="346" height="42" rx="8" fill="#0a192c" stroke="#38bdf8" stroke-opacity="0.35" stroke-width="1"/>
            <text x="16" y="26" fill="#38bdf8" class="about-mono" font-size="10.5" font-weight="700" letter-spacing="0.5">ETHOS: Rigor · Curiosity · Neural Systems</text>
          </g>
        </g>
      </g>
    </g>

    <!-- Outer Frame Stroke -->
    <rect x="1" y="1" width="878" height="368" rx="15" fill="none" stroke="url(#about-border-grad)" stroke-width="1.5" style="animation: border-breathe 4s infinite ease-in-out;"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. STACK.SVG
# -------------------------------------------------------------
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1672 941" width="100%" height="auto" fill="none">
  <defs>
    <linearGradient id="stack-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#1e293b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>
    <clipPath id="stack-rounded">
      <rect width="1672" height="941" rx="20" ry="20" />
    </clipPath>
  </defs>
  <g clip-path="url(#stack-rounded)">
    <image href="{stack_b64}" width="1672" height="941" />
    <rect x="1" y="1" width="1670" height="939" rx="19" fill="none" stroke="url(#stack-border-grad)" stroke-width="2" />
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. ID-DASHBOARD.SVG
# -------------------------------------------------------------
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1765 891" width="100%" height="auto" fill="none">
  <defs>
    <style>
      @keyframes foil-sweep {{
        0% {{ transform: translateX(-120%) rotate(25deg); opacity: 0; }}
        15% {{ opacity: 0.45; }}
        35% {{ transform: translateX(260%) rotate(25deg); opacity: 0; }}
        100% {{ transform: translateX(260%) rotate(25deg); opacity: 0; }}
      }}
      @keyframes beacon-ping {{
        0% {{ r: 4px; opacity: 1; stroke-width: 2.5px; }}
        70% {{ r: 16px; opacity: 0; stroke-width: 0.5px; }}
        100% {{ r: 16px; opacity: 0; stroke-width: 0px; }}
      }}
      @keyframes border-glow {{
        0%, 100% {{ stroke-opacity: 0.6; }}
        50% {{ stroke-opacity: 1; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
      }}
    </style>

    <linearGradient id="id-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#1e293b" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.9"/>
    </linearGradient>

    <!-- Holographic Foil Shimmer -->
    <linearGradient id="foil-shimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="40%" stop-color="#00d8ff" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.45"/>
      <stop offset="60%" stop-color="#ff354f" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <!-- Rounded Canvas Clip -->
    <clipPath id="main-rounded-clip">
      <rect width="1765" height="891" rx="26" ry="26" />
    </clipPath>

    <!-- ID Card Lanyard Badge Clip for Foil Effect -->
    <clipPath id="badge-foil-clip">
      <rect x="70" y="160" width="455" height="675" rx="36" ry="36" />
    </clipPath>
  </defs>

  <g clip-path="url(#main-rounded-clip)">
    <!-- Base 3D Render Image (Full HD Retina Fidelity) -->
    <image href="{profiles_b64}" width="1765" height="891" />

    <!-- ==================== ANIMATED LAYER: ID BADGE HOLOGRAPHIC SWEEP ==================== -->
    <g clip-path="url(#badge-foil-clip)">
      <rect x="-200" y="-100" width="280" height="1200" fill="url(#foil-shimmer)" style="animation: foil-sweep 6s infinite cubic-bezier(0.4, 0, 0.2, 1);" />
    </g>

    <!-- ==================== ANIMATED LAYER: PULSING RADAR BEACONS ==================== -->
    
    <!-- 1. Top-Right "VERIFIED" Green Dot (x=1602, y=77) -->
    <g transform="translate(1602, 77)">
      <circle cx="0" cy="0" r="4.5" fill="#00ff88" />
      <circle cx="0" cy="0" r="5" fill="none" stroke="#00ff88" style="animation: beacon-ping 2.4s infinite ease-out;" />
      <circle cx="0" cy="0" r="5" fill="none" stroke="#00ff88" style="animation: beacon-ping 2.4s infinite ease-out 1.2s;" />
    </g>

    <!-- 2. ID Card Online Indicator (x=472, y=268) -->
    <g transform="translate(472, 268)">
      <circle cx="0" cy="0" r="8" fill="#00ff88" />
      <circle cx="0" cy="0" r="8" fill="none" stroke="#00ff88" style="animation: beacon-ping 3s infinite ease-out;" />
      <circle cx="0" cy="0" r="8" fill="none" stroke="#00ff88" style="animation: beacon-ping 3s infinite ease-out 1.5s;" />
    </g>

    <!-- 3. Bottom Status Beacon (x=622, y=788) -->
    <g transform="translate(622, 788)">
      <circle cx="0" cy="0" r="6" fill="#00ff88" />
      <circle cx="0" cy="0" r="6" fill="none" stroke="#00ff88" style="animation: beacon-ping 2.8s infinite ease-out;" />
      <circle cx="0" cy="0" r="6" fill="none" stroke="#00ff88" style="animation: beacon-ping 2.8s infinite ease-out 1.4s;" />
    </g>

    <!-- ==================== ANIMATED LAYER: AMBIENT NEON FRAME GLOW ==================== -->
    <rect x="1.5" y="1.5" width="1762" height="888" rx="25" fill="none" stroke="url(#id-border-grad)" stroke-width="2.5" style="animation: border-glow 4s ease-in-out infinite;" />
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. CONNECT.SVG
# -------------------------------------------------------------
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 360" width="880" height="360" fill="none">
  <defs>
    <style>
      .conn-font {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      }}
      .conn-mono {{
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
      }}

      @keyframes arrow-nudge {{
        0%, 100% {{ transform: translateX(0px); opacity: 0.6; }}
        50% {{ transform: translateX(6px); opacity: 1; }}
      }}
      @keyframes char-breathe {{
        0%, 100% {{ transform: translateY(0px) scale(1); }}
        50% {{ transform: translateY(-4px) scale(1.008); }}
      }}
      @keyframes card-glow {{
        0%, 100% {{ stroke-opacity: 0.4; }}
        50% {{ stroke-opacity: 0.9; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
      }}
    </style>

    <linearGradient id="conn-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060914"/>
      <stop offset="50%" stop-color="#091222"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>

    <linearGradient id="conn-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="50%" stop-color="#1e2a44"/>
      <stop offset="100%" stop-color="#ff354f"/>
    </linearGradient>

    <radialGradient id="conn-char-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <clipPath id="conn-main-clip">
      <rect x="0" y="0" width="880" height="360" rx="16"/>
    </clipPath>
  </defs>

  <g clip-path="url(#conn-main-clip)">
    <!-- Background -->
    <rect width="880" height="360" fill="url(#conn-bg-grad)"/>

    <!-- Section Header Tag -->
    <g transform="translate(42, 26)">
      <rect x="0" y="0" width="165" height="26" rx="6" fill="#0d182b" stroke="#247bff" stroke-opacity="0.4" stroke-width="1"/>
      <text x="12" y="17" fill="#58a6ff" class="conn-mono" font-size="10.5" font-weight="700" letter-spacing="1">05 // LET'S CONNECT</text>
      <text x="185" y="18" fill="#8b949e" class="conn-font" font-size="13">Explore videos, community updates, codebases and collaborations</text>
    </g>

    <!-- LEFT: POINTING CHARACTER (right_pointing.png) -->
    <g transform="translate(15, 50)">
      <ellipse cx="160" cy="180" rx="140" ry="110" fill="url(#conn-char-glow)"/>
      <g style="animation: char-breathe 4.5s ease-in-out infinite;">
        <image href="{pointing_b64}" x="0" y="0" width="370" height="310" preserveAspectRatio="xMidYMid meet"/>
      </g>
    </g>

    <!-- RIGHT: SOCIAL CARDS COLUMN -->
    <g transform="translate(410, 64)">
      
      <!-- CARD 1: YOUTUBE -->
      <g transform="translate(0, 0)">
        <rect width="428" height="68" rx="12" fill="#0b1322" stroke="#ff0000" stroke-opacity="0.45" stroke-width="1.2" style="animation: card-glow 4s infinite ease-in-out;"/>
        <rect x="16" y="14" width="40" height="40" rx="8" fill="#280c0e" stroke="#ff0000" stroke-opacity="0.6"/>
        <path d="M43 34C43 31.8 42.8 29.5 42.4 28.5C42 27.2 40.8 26 39.5 25.6C38 25 36 25 36 25C36 25 34 25 32.5 25.6C31.2 26 30 27.2 29.6 28.5C29.2 29.5 29 31.8 29 34C29 36.2 29.2 38.5 29.6 39.5C30 40.8 31.2 42 32.5 42.4C34 43 36 43 36 43C36 43 38 43 39.5 42.4C40.8 42 42 40.8 42.4 39.5C42.8 38.5 43 36.2 43 34ZM34.5 38V30L40 34L34.5 38Z" fill="#ff354f"/>
        
        <text x="68" y="32" fill="#ffffff" class="conn-font" font-size="14" font-weight="700">YouTube // Divyansh-Codespace</text>
        <text x="68" y="49" fill="#8b949e" class="conn-font" font-size="11.5">Tech tutorials, AI builds, and coding walkthroughs</text>
        
        <g transform="translate(388, 34)" style="animation: arrow-nudge 1.8s infinite ease-in-out;">
          <path d="M-6 -6L0 0L-6 6" stroke="#ff354f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
      </g>

      <!-- CARD 2: INSTAGRAM -->
      <g transform="translate(0, 78)">
        <rect width="428" height="68" rx="12" fill="#0b1322" stroke="#e1306c" stroke-opacity="0.45" stroke-width="1.2" style="animation: card-glow 4s infinite 1.3s ease-in-out;"/>
        <rect x="16" y="14" width="40" height="40" rx="8" fill="#250e18" stroke="#e1306c" stroke-opacity="0.6"/>
        <rect x="27" y="25" width="18" height="18" rx="5" fill="none" stroke="#ff4d8b" stroke-width="1.8"/>
        <circle cx="36" cy="34" r="4.5" fill="none" stroke="#ff4d8b" stroke-width="1.8"/>
        <circle cx="41.5" cy="29.5" r="1" fill="#ff4d8b"/>

        <text x="68" y="32" fill="#ffffff" class="conn-font" font-size="14" font-weight="700">Instagram // @ryth.core</text>
        <text x="68" y="49" fill="#8b949e" class="conn-font" font-size="11.5">Product growth, founder journey &amp; behind-the-scenes</text>

        <g transform="translate(388, 34)" style="animation: arrow-nudge 1.8s infinite 0.6s ease-in-out;">
          <path d="M-6 -6L0 0L-6 6" stroke="#ff4d8b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
      </g>

      <!-- CARD 3: GITHUB REPOSITORIES -->
      <g transform="translate(0, 156)">
        <rect width="428" height="68" rx="12" fill="#0b1322" stroke="#247bff" stroke-opacity="0.45" stroke-width="1.2" style="animation: card-glow 4s infinite 2.6s ease-in-out;"/>
        <rect x="16" y="14" width="40" height="40" rx="8" fill="#0d182b" stroke="#247bff" stroke-opacity="0.6"/>
        <path d="M36 24C30.5 24 26 28.5 26 34C26 38.4 28.9 42.1 32.8 43.4C33.3 43.5 33.5 43.2 33.5 42.9C33.5 42.7 33.5 41.9 33.5 40.9C30.7 41.5 30.1 39.6 30.1 39.6C29.6 38.4 29 38.1 29 38.1C28.1 37.5 29.1 37.5 29.1 37.5C30.1 37.6 30.6 38.5 30.6 38.5C31.5 40 33 39.6 33.6 39.3C33.7 38.6 33.9 38.2 34.3 37.9C32.1 37.6 29.7 36.8 29.7 33C29.7 31.9 30.1 31 30.7 30.3C30.6 30.1 30.3 29.1 30.8 27.7C30.8 27.7 31.7 27.4 33.7 28.7C34.5 28.5 35.4 28.4 36.3 28.4C37.2 28.4 38.1 28.5 38.9 28.7C40.9 27.4 41.8 27.7 41.8 27.7C42.3 29.1 42 30.1 41.9 30.3C42.6 31 42.9 31.9 42.9 33C42.9 36.8 40.6 37.6 38.3 37.8C38.7 38.2 39.1 38.9 39.1 40C39.1 41.6 39.1 42.9 39.1 43.3C39.1 43.6 39.3 43.9 39.8 43.8C43.7 42.5 46.6 38.8 46.6 34.4C46.6 28.5 42.1 24 36.6 24H36Z" fill="#58a6ff"/>

        <text x="68" y="32" fill="#ffffff" class="conn-font" font-size="14" font-weight="700">GitHub // @divyansh-x-codes</text>
        <text x="68" y="49" fill="#8b949e" class="conn-font" font-size="11.5">Open source code, AI repositories &amp; experiments</text>

        <g transform="translate(388, 34)" style="animation: arrow-nudge 1.8s infinite 1.2s ease-in-out;">
          <path d="M-6 -6L0 0L-6 6" stroke="#58a6ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
      </g>

      <!-- Bottom Direct Message Pill -->
      <g transform="translate(0, 234)">
        <rect width="428" height="34" rx="8" fill="#080e1b" stroke="#1c2b48" stroke-width="1"/>
        <circle cx="20" cy="17" r="4" fill="#00ff88"/>
        <text x="34" y="21" fill="#c9d1d9" class="conn-font" font-size="11.5" font-weight="500">✨ Click the social links below the banner to connect directly!</text>
      </g>
    </g>

    <!-- Outer Frame Stroke -->
    <rect x="1" y="1" width="878" height="358" rx="15" fill="none" stroke="url(#conn-border-grad)" stroke-width="1.5"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# Write SVG files
# -------------------------------------------------------------
svg_files = {
    "hero.svg": hero_svg,
    "about-life.svg": about_life_svg,
    "stack.svg": stack_svg,
    "id-dashboard.svg": id_dashboard_svg,
    "connect.svg": connect_svg,
}

for fname, content in svg_files.items():
    fpath = os.path.join(ASSETS_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {fpath} ({len(content)} bytes)")

# Update README.md with ?v=3 to bust GitHub cache
readme_content = '''<div align="center">

<!-- HERO SECTION -->
![Divyansh Chaudhary - Intro](./assets/hero.svg?v=10)

<!-- ABOUT & LIFE CAROUSEL -->
![About & Capabilities](./assets/about-life.svg?v=10)

<!-- TECH ARSENAL ORBIT -->
![System Tech Arsenal](./assets/stack.svg?v=10)

<!-- VERIFIED ID & TELEMETRY DASHBOARD -->
![Verified ID Dashboard](./assets/id-dashboard.svg?v=10)

<!-- CONNECT & COLLABORATE -->
![Let's Connect](./assets/connect.svg?v=10)

<br/>

### 🌐 Direct Connect & Social Links

[![YouTube](https://img.shields.io/badge/YouTube-@Divyansh--Codespace-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@Divyansh-Codespace)
[![Instagram](https://img.shields.io/badge/Instagram-@ryth.core-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ryth.core/)
[![GitHub](https://img.shields.io/badge/GitHub-divyansh--x--codes-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/divyansh-x-codes)

</div>

<br/>

---

### 🚀 Featured Systems & Projects

| Project | Domain | Architecture / Stack | Description & Impact |
| :--- | :--- | :--- | :--- |
| **[Ryth](https://www.instagram.com/ryth.core/)** | **Platform / Growth** | `React` `Node.js` `AI Engine` `SQL` | Subscription-based content & personal growth platform featuring smart feeds, habit tracking, creator ecosystems, and verified production backend serving **200+ users**. |
| **[Neural AI Pipeline](https://github.com/divyansh-x-codes)** | **AI / Deep Learning** | `Python` `TensorFlow` `scikit-learn` | End-to-end intelligent machine learning workflows, computer vision models, predictive intelligence, and high-throughput data training pipelines. |
| **[High-Performance Systems](https://github.com/divyansh-x-codes)** | **Systems / Algorithms** | `C++` `Data Structures` `Algorithms` | Optimized algorithmic implementations, low-level computation routines, memory-efficient data processing, and scalable backend modules. |

---

<div align="center">
  <sub>Crafted with passion, neural intelligence, and clean code · © 2026 <b>Divyansh Chaudhary</b></sub>
</div>
'''

readme_path = os.path.join(WORKSPACE, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content.strip())
print(f"Generated: {readme_path}")
