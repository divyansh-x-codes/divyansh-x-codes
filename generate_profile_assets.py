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

      /* Carousel Progress Bar Animations (12s cycle: 4s each) */
      @keyframes prog1 {{
        0% {{ width: 0%; }}
        30%, 100% {{ width: 100%; }}
      }}
      @keyframes prog2 {{
        0%, 33.3% {{ width: 0%; }}
        63.3%, 100% {{ width: 100%; }}
      }}
      @keyframes prog3 {{
        0%, 66.6% {{ width: 0%; }}
        96.6%, 100% {{ width: 100%; }}
      }}

      /* Carousel Slide Transitions */
      @keyframes slide1 {{
        0%, 30% {{ opacity: 1; transform: translateX(0); }}
        33.3%, 97% {{ opacity: 0; transform: translateX(16px); pointer-events: none; }}
        100% {{ opacity: 1; transform: translateX(0); }}
      }}
      @keyframes slide2 {{
        0%, 30% {{ opacity: 0; transform: translateX(-16px); pointer-events: none; }}
        33.3%, 63.3% {{ opacity: 1; transform: translateX(0); }}
        66.6%, 100% {{ opacity: 0; transform: translateX(16px); pointer-events: none; }}
      }}
      @keyframes slide3 {{
        0%, 63.3% {{ opacity: 0; transform: translateX(-16px); pointer-events: none; }}
        66.6%, 96.6% {{ opacity: 1; transform: translateX(0); }}
        100% {{ opacity: 0; transform: translateX(16px); pointer-events: none; }}
      }}

      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
      }}
    </style>

    <linearGradient id="about-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060a14"/>
      <stop offset="100%" stop-color="#0b1424"/>
    </linearGradient>

    <linearGradient id="about-card-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0e192f"/>
      <stop offset="100%" stop-color="#080e1c"/>
    </linearGradient>

    <linearGradient id="about-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#1b253b"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.6"/>
    </linearGradient>

    <pattern id="about-grid" width="22" height="22" patternUnits="userSpaceOnUse">
      <path d="M 22 0 L 0 0 0 22" fill="none" stroke="#247bff" stroke-opacity="0.06" stroke-width="1"/>
    </pattern>

    <clipPath id="about-main-clip">
      <rect x="0" y="0" width="880" height="370" rx="16"/>
    </clipPath>
  </defs>

  <g clip-path="url(#about-main-clip)">
    <!-- Main Background -->
    <rect width="880" height="370" fill="url(#about-bg-grad)"/>
    <rect width="880" height="370" fill="url(#about-grid)"/>

    <!-- Section Header Tag (Pill width 225px to avoid text overlap) -->
    <g transform="translate(42, 26)">
      <rect x="0" y="0" width="215" height="26" rx="6" fill="#0e1a30" stroke="#247bff" stroke-opacity="0.4" stroke-width="1"/>
      <text x="12" y="17" fill="#58a6ff" class="about-mono" font-size="10.5" font-weight="700" letter-spacing="1">02 // CAPABILITIES &amp; LIFE</text>
      <text x="235" y="18" fill="#8b949e" class="about-font" font-size="13">What drives my technical craftsmanship and daily curiosity</text>
    </g>

    <!-- LEFT CARD: CAPABILITIES -->
    <g transform="translate(42, 68)">
      <rect width="386" height="272" rx="14" fill="url(#about-card-grad)" stroke="#1a2742" stroke-width="1.2"/>
      
      <!-- Card Title -->
      <text x="22" y="30" fill="#ffffff" class="about-font" font-size="15" font-weight="800" letter-spacing="0.5">CORE CAPABILITIES</text>
      <text x="325" y="30" fill="#247bff" class="about-mono" font-size="11.5" font-weight="700">SPEC</text>
      <line x1="22" y1="44" x2="364" y2="44" stroke="#16233b" stroke-width="1"/>

      <!-- Capability 1 -->
      <g transform="translate(22, 58)">
        <rect x="0" y="0" width="34" height="34" rx="8" fill="#13233f" stroke="#247bff" stroke-opacity="0.5"/>
        <path d="M12 17C12 14.2 14.2 12 17 12C19.8 12 22 14.2 22 17C22 19.8 19.8 22 17 22" stroke="#58a6ff" stroke-width="2" stroke-linecap="round"/>
        <circle cx="17" cy="17" r="2" fill="#00ff88"/>
        <text x="46" y="15" fill="#f0f6fc" class="about-font" font-size="13" font-weight="700">Applied AI &amp; Machine Learning</text>
        <text x="46" y="31" fill="#8b949e" class="about-font" font-size="11">TensorFlow, Scikit-learn, Neural Nets &amp; Vision</text>
      </g>

      <!-- Capability 2 -->
      <g transform="translate(22, 124)">
        <rect x="0" y="0" width="34" height="34" rx="8" fill="#241424" stroke="#ff354f" stroke-opacity="0.5"/>
        <path d="M11 14L17 10L23 14L17 18L11 14ZM11 20L17 24L23 20" stroke="#ff354f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="46" y="15" fill="#f0f6fc" class="about-font" font-size="13" font-weight="700">Full-Stack Architecture</text>
        <text x="46" y="31" fill="#8b949e" class="about-font" font-size="11">React, Node.js, REST APIs, High Performance</text>
      </g>

      <!-- Capability 3 -->
      <g transform="translate(22, 190)">
        <rect x="0" y="0" width="34" height="34" rx="8" fill="#0f262a" stroke="#00ff88" stroke-opacity="0.5"/>
        <path d="M17 10V24M10 17H24" stroke="#00ff88" stroke-width="2" stroke-linecap="round"/>
        <text x="46" y="15" fill="#f0f6fc" class="about-font" font-size="13" font-weight="700">Systems, Algorithms &amp; C++</text>
        <text x="46" y="31" fill="#8b949e" class="about-font" font-size="11">Low-level efficiency, Clean Code &amp; Git ELT</text>
      </g>
    </g>

    <!-- RIGHT CARD: 3-SLIDE INTERESTS CAROUSEL -->
    <g transform="translate(452, 68)">
      <rect width="386" height="272" rx="14" fill="url(#about-card-grad)" stroke="#1a2742" stroke-width="1.2"/>
      
      <!-- Top Title & Progress Bars Section -->
      <g transform="translate(22, 18)">
        <text x="0" y="12" fill="#ffffff" class="about-font" font-size="15" font-weight="800" letter-spacing="0.5">INTERESTS &amp; PASSIONS</text>
        
        <!-- Segment Progress Indicators (3 Bars) -->
        <g transform="translate(0, 24)">
          <!-- Seg 1 -->
          <rect x="0" y="0" width="108" height="4" rx="2" fill="#1a2744"/>
          <rect x="0" y="0" height="4" rx="2" fill="#247bff" style="animation: prog1 12s infinite linear;"/>

          <!-- Seg 2 -->
          <rect x="118" y="0" width="108" height="4" rx="2" fill="#1a2744"/>
          <rect x="118" y="0" height="4" rx="2" fill="#ff354f" style="animation: prog2 12s infinite linear;"/>

          <!-- Seg 3 -->
          <rect x="236" y="0" width="108" height="4" rx="2" fill="#1a2744"/>
          <rect x="236" y="0" height="4" rx="2" fill="#00ff88" style="animation: prog3 12s infinite linear;"/>
        </g>
      </g>

      <line x1="22" y1="58" x2="364" y2="58" stroke="#16233b" stroke-width="1"/>

      <!-- CAROUSEL SLIDES (Positioned comfortably below separator) -->
      
      <!-- SLIDE 1: AI & ML -->
      <g transform="translate(22, 72)" style="animation: slide1 12s infinite cubic-bezier(0.4, 0, 0.2, 1);">
        <!-- Tag -->
        <rect x="0" y="0" width="86" height="22" rx="4" fill="#13233f"/>
        <text x="8" y="15" fill="#58a6ff" class="about-mono" font-size="10" font-weight="700">01 / PASSION</text>
        
        <!-- Title -->
        <text x="0" y="44" fill="#ffffff" class="about-font" font-size="18" font-weight="800">AI &amp; Machine Learning</text>
        
        <!-- Description -->
        <text x="0" y="68" fill="#a0aec0" class="about-font" font-size="12.5">Fascinated by neural networks, predictive intelligence,</text>
        <text x="0" y="86" fill="#a0aec0" class="about-font" font-size="12.5">and transforming raw data into actionable decision systems.</text>

        <!-- Bottom Pill -->
        <g transform="translate(0, 110)">
          <rect x="0" y="0" width="342" height="32" rx="6" fill="#070c18" stroke="#1f2d48" stroke-width="1"/>
          <text x="12" y="20" fill="#58a6ff" class="about-mono" font-size="10.5">FOCUS: Deep Learning · Computer Vision · NLP</text>
        </g>
      </g>

      <!-- SLIDE 2: CAR RACING -->
      <g transform="translate(22, 72)" style="animation: slide2 12s infinite cubic-bezier(0.4, 0, 0.2, 1);">
        <!-- Tag -->
        <rect x="0" y="0" width="98" height="22" rx="4" fill="#29121a"/>
        <text x="8" y="15" fill="#ff4d6a" class="about-mono" font-size="10" font-weight="700">02 / ADRENALINE</text>
        
        <!-- Title -->
        <text x="0" y="44" fill="#ffffff" class="about-font" font-size="18" font-weight="800">Car Racing &amp; Dynamics</text>
        
        <!-- Description -->
        <text x="0" y="68" fill="#a0aec0" class="about-font" font-size="12.5">The thrill of high-speed aerodynamics, apex precision,</text>
        <text x="0" y="86" fill="#a0aec0" class="about-font" font-size="12.5">and high-stakes split-second decision making under pressure.</text>

        <!-- Bottom Pill -->
        <g transform="translate(0, 110)">
          <rect x="0" y="0" width="342" height="32" rx="6" fill="#070c18" stroke="#1f2d48" stroke-width="1"/>
          <text x="12" y="20" fill="#ff4d6a" class="about-mono" font-size="10.5">ETHOS: Speed · Telemetry · Peak Precision</text>
        </g>
      </g>

      <!-- SLIDE 3: ENTREPRENEURSHIP -->
      <g transform="translate(22, 72)" style="animation: slide3 12s infinite cubic-bezier(0.4, 0, 0.2, 1);">
        <!-- Tag -->
        <rect x="0" y="0" width="92" height="22" rx="4" fill="#0c231e"/>
        <text x="8" y="15" fill="#00ff88" class="about-mono" font-size="10" font-weight="700">03 / VENTURES</text>
        
        <!-- Title -->
        <text x="0" y="44" fill="#ffffff" class="about-font" font-size="18" font-weight="800">Entrepreneurship &amp; Building</text>
        
        <!-- Description -->
        <text x="0" y="68" fill="#a0aec0" class="about-font" font-size="12.5">Founder of Ryth (200+ active users). Building products</text>
        <text x="0" y="86" fill="#a0aec0" class="about-font" font-size="12.5">that blend user growth, smart content and intuitive design.</text>

        <!-- Bottom Pill -->
        <g transform="translate(0, 110)">
          <rect x="0" y="0" width="342" height="32" rx="6" fill="#070c18" stroke="#1f2d48" stroke-width="1"/>
          <text x="12" y="20" fill="#00ff88" class="about-mono" font-size="10.5">VENTURE: Ryth Platform · Growth &amp; Tech</text>
        </g>
      </g>
    </g>

    <!-- Outer Border -->
    <rect x="1" y="1" width="878" height="368" rx="15" fill="none" stroke="url(#about-border-grad)" stroke-width="1.5"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. STACK.SVG
# -------------------------------------------------------------
stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 400" width="880" height="400" fill="none">
  <defs>
    <style>
      .stack-font {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      }}
      .stack-mono {{
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
      }}
      @keyframes orbit-pulse {{
        0%, 100% {{ opacity: 0.4; transform: scale(1); }}
        50% {{ opacity: 0.9; transform: scale(1.08); }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
      }}
    </style>

    <linearGradient id="stack-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050913"/>
      <stop offset="50%" stop-color="#091224"/>
      <stop offset="100%" stop-color="#060a15"/>
    </linearGradient>

    <linearGradient id="stack-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#1c263c"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="stack-center-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#ff354f"/>
    </linearGradient>

    <clipPath id="stack-card-clip">
      <rect x="0" y="0" width="880" height="400" rx="16"/>
    </clipPath>
  </defs>

  <g clip-path="url(#stack-card-clip)">
    <!-- Background -->
    <rect width="880" height="400" fill="url(#stack-bg-grad)"/>

    <!-- Header -->
    <g transform="translate(42, 26)">
      <rect x="0" y="0" width="170" height="26" rx="6" fill="#0d182b" stroke="#247bff" stroke-opacity="0.4" stroke-width="1"/>
      <text x="12" y="17" fill="#58a6ff" class="stack-mono" font-size="10.5" font-weight="700" letter-spacing="1">03 // TECH ARSENAL</text>
      <text x="190" y="18" fill="#8b949e" class="stack-font" font-size="13">Core languages, AI/ML frameworks, and platform tooling</text>
    </g>

    <!-- CENTER PLANETARY ORBIT SYSTEM -->
    <g transform="translate(440, 140)">
      <circle cx="0" cy="0" r="110" fill="#247bff" fill-opacity="0.08"/>

      <!-- Orbit 1: Inner -->
      <ellipse cx="0" cy="0" rx="135" ry="46" fill="none" stroke="#247bff" stroke-opacity="0.3" stroke-width="1.2" stroke-dasharray="4 4" transform="rotate(-15)"/>

      <!-- Orbit 2: Middle -->
      <ellipse cx="0" cy="0" rx="230" ry="62" fill="none" stroke="#58a6ff" stroke-opacity="0.25" stroke-width="1.2" stroke-dasharray="6 6" transform="rotate(8)"/>

      <!-- Orbit 3: Outer -->
      <ellipse cx="0" cy="0" rx="320" ry="78" fill="none" stroke="#ff354f" stroke-opacity="0.25" stroke-width="1.2" stroke-dasharray="8 6" transform="rotate(-6)"/>

      <!-- Node: Python -->
      <g transform="translate(-165, -42)">
        <circle cx="0" cy="0" r="18" fill="#0a162a" stroke="#247bff" stroke-width="1.5"/>
        <text x="0" y="4" text-anchor="middle" fill="#58a6ff" class="stack-mono" font-size="10.5" font-weight="700">PY</text>
        <text x="0" y="27" text-anchor="middle" fill="#c9d1d9" class="stack-font" font-size="10" font-weight="600">Python</text>
      </g>

      <!-- Node: TensorFlow -->
      <g transform="translate(175, -35)">
        <circle cx="0" cy="0" r="19" fill="#1f1414" stroke="#ff7b72" stroke-width="1.5"/>
        <text x="0" y="4" text-anchor="middle" fill="#ff7b72" class="stack-mono" font-size="10.5" font-weight="700">TF</text>
        <text x="0" y="27" text-anchor="middle" fill="#c9d1d9" class="stack-font" font-size="10" font-weight="600">TensorFlow</text>
      </g>

      <!-- Node: C++ -->
      <g transform="translate(-280, 10)">
        <circle cx="0" cy="0" r="18" fill="#0c182b" stroke="#00d8ff" stroke-width="1.5"/>
        <text x="0" y="4" text-anchor="middle" fill="#00d8ff" class="stack-mono" font-size="10" font-weight="700">C++</text>
        <text x="0" y="27" text-anchor="middle" fill="#c9d1d9" class="stack-font" font-size="10" font-weight="600">C / C++</text>
      </g>

      <!-- Node: React -->
      <g transform="translate(290, 12)">
        <circle cx="0" cy="0" r="18" fill="#091b2c" stroke="#61dafb" stroke-width="1.5"/>
        <text x="0" y="4" text-anchor="middle" fill="#61dafb" class="stack-mono" font-size="10" font-weight="700">RCT</text>
        <text x="0" y="27" text-anchor="middle" fill="#c9d1d9" class="stack-font" font-size="10" font-weight="600">React</text>
      </g>

      <!-- Node: Scikit-learn -->
      <g transform="translate(-65, 48)">
        <circle cx="0" cy="0" r="17" fill="#1b1d12" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="0" y="4" text-anchor="middle" fill="#f59e0b" class="stack-mono" font-size="10" font-weight="700">SKL</text>
        <text x="0" y="27" text-anchor="middle" fill="#c9d1d9" class="stack-font" font-size="10" font-weight="600">Scikit-Learn</text>
      </g>

      <!-- Node: Node.js -->
      <g transform="translate(90, 45)">
        <circle cx="0" cy="0" r="17" fill="#0c1e14" stroke="#00ff88" stroke-width="1.5"/>
        <text x="0" y="4" text-anchor="middle" fill="#00ff88" class="stack-mono" font-size="10" font-weight="700">JS</text>
        <text x="0" y="27" text-anchor="middle" fill="#c9d1d9" class="stack-font" font-size="10" font-weight="600">Node / JS</text>
      </g>

      <!-- Core Center Star -->
      <circle cx="0" cy="0" r="32" fill="url(#stack-center-grad)"/>
      <circle cx="0" cy="0" r="36" fill="none" stroke="#ffffff" stroke-opacity="0.3" stroke-width="1.5" style="animation: orbit-pulse 3s infinite ease-in-out;"/>
      <text x="0" y="5" text-anchor="middle" fill="#ffffff" class="stack-font" font-size="12" font-weight="900" letter-spacing="0.5">CORE</text>
    </g>

    <!-- BOTTOM SECTION: GROUPED TECH CHIPS -->
    <g transform="translate(42, 252)">
      <rect width="796" height="120" rx="12" fill="#0b1322" stroke="#16233a" stroke-width="1"/>
      
      <text x="18" y="24" fill="#8b949e" class="stack-mono" font-size="10.5" font-weight="600" letter-spacing="0.5">PROVEN PROFICIENCIES // PRODUCTION &amp; RESEARCH</text>

      <!-- Row 1: Languages & AI/ML -->
      <g transform="translate(18, 38)">
        <!-- Python -->
        <g transform="translate(0, 0)">
          <rect width="144" height="30" rx="6" fill="#0f1b30" stroke="#247bff" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#388bfd"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">Python 3</text>
          <text x="96" y="19" fill="#58a6ff" class="stack-mono" font-size="9.5">AI/Core</text>
        </g>
        <!-- C++ -->
        <g transform="translate(154, 0)">
          <rect width="144" height="30" rx="6" fill="#0f1b30" stroke="#00d8ff" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#00d8ff"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">C / C++</text>
          <text x="96" y="19" fill="#00d8ff" class="stack-mono" font-size="9.5">Perf</text>
        </g>
        <!-- TensorFlow -->
        <g transform="translate(308, 0)">
          <rect width="154" height="30" rx="6" fill="#1e1416" stroke="#ff354f" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#ff354f"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">TensorFlow</text>
          <text x="108" y="19" fill="#ff7b72" class="stack-mono" font-size="9.5">Neural</text>
        </g>
        <!-- Scikit-learn -->
        <g transform="translate(472, 0)">
          <rect width="148" height="30" rx="6" fill="#1f1a10" stroke="#f59e0b" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#f59e0b"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">scikit-learn</text>
          <text x="110" y="19" fill="#f59e0b" class="stack-mono" font-size="9.5">ML</text>
        </g>
        <!-- SQL -->
        <g transform="translate(630, 0)">
          <rect width="130" height="30" rx="6" fill="#0f1b30" stroke="#247bff" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#58a6ff"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">SQL / DB</text>
        </g>
      </g>

      <!-- Row 2: Web & Tools -->
      <g transform="translate(18, 76)">
        <!-- React -->
        <g transform="translate(0, 0)">
          <rect width="144" height="30" rx="6" fill="#0a1a2b" stroke="#61dafb" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#61dafb"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">React.js</text>
          <text x="96" y="19" fill="#61dafb" class="stack-mono" font-size="9.5">UI/UX</text>
        </g>
        <!-- Node.js -->
        <g transform="translate(154, 0)">
          <rect width="144" height="30" rx="6" fill="#0c1e14" stroke="#00ff88" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#00ff88"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">Node.js</text>
          <text x="94" y="19" fill="#00ff88" class="stack-mono" font-size="9.5">Backend</text>
        </g>
        <!-- JavaScript -->
        <g transform="translate(308, 0)">
          <rect width="154" height="30" rx="6" fill="#1e1e0f" stroke="#eab308" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#eab308"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">JavaScript ES6+</text>
        </g>
        <!-- Git -->
        <g transform="translate(472, 0)">
          <rect width="148" height="30" rx="6" fill="#1e1414" stroke="#f05032" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#f05032"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">Git / VCS</text>
        </g>
        <!-- GitHub -->
        <g transform="translate(630, 0)">
          <rect width="130" height="30" rx="6" fill="#161b22" stroke="#8b949e" stroke-opacity="0.6" stroke-width="1"/>
          <circle cx="15" cy="15" r="4" fill="#c9d1d9"/>
          <text x="28" y="19" fill="#f0f6fc" class="stack-font" font-size="11.5" font-weight="600">GitHub CI/CD</text>
        </g>
      </g>
    </g>

    <!-- Outer Frame Stroke -->
    <rect x="1" y="1" width="878" height="398" rx="15" fill="none" stroke="url(#stack-border-grad)" stroke-width="1.5"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. ID-DASHBOARD.SVG
# -------------------------------------------------------------
id_dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 430" width="880" height="430" fill="none">
  <defs>
    <style>
      .id-font {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      }}
      .id-mono {{
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
      }}

      @keyframes lanyard-gentle-swing {{
        0%, 100% {{ transform: rotate(-1.7deg); }}
        50% {{ transform: rotate(1.7deg); }}
      }}
      @keyframes foil-sweep {{
        0% {{ transform: translateX(-150%) rotate(25deg); opacity: 0; }}
        20% {{ opacity: 0.6; }}
        40% {{ transform: translateX(250%) rotate(25deg); opacity: 0; }}
        100% {{ transform: translateX(250%) rotate(25deg); opacity: 0; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; }}
      }}
    </style>

    <linearGradient id="id-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060914"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>

    <linearGradient id="id-card-foil" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f1b33"/>
      <stop offset="50%" stop-color="#142445"/>
      <stop offset="100%" stop-color="#091122"/>
    </linearGradient>

    <linearGradient id="id-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="50%" stop-color="#1a2742"/>
      <stop offset="100%" stop-color="#ff354f"/>
    </linearGradient>

    <linearGradient id="id-shimmer-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <clipPath id="id-main-clip">
      <rect x="0" y="0" width="880" height="430" rx="16"/>
    </clipPath>

    <clipPath id="id-badge-clip">
      <rect x="0" y="0" width="220" height="320" rx="14"/>
    </clipPath>

    <clipPath id="id-badge-photo-clip">
      <rect x="0" y="0" width="192" height="150" rx="10"/>
    </clipPath>
  </defs>

  <g clip-path="url(#id-main-clip)">
    <!-- Main Background -->
    <rect width="880" height="430" fill="url(#id-bg-grad)"/>

    <!-- Section Header Tag -->
    <g transform="translate(42, 26)">
      <rect x="0" y="0" width="180" height="26" rx="6" fill="#0d182b" stroke="#247bff" stroke-opacity="0.4" stroke-width="1"/>
      <text x="12" y="17" fill="#58a6ff" class="id-mono" font-size="10.5" font-weight="700" letter-spacing="1">04 // VERIFIED CREDENTIALS</text>
      <text x="200" y="18" fill="#8b949e" class="id-font" font-size="13">Cryptographically verified metrics, builder stats &amp; credentials</text>
    </g>

    <!-- LEFT: HANGING LANYARD ID BADGE -->
    <g transform="translate(170, 55)">
      <path d="M-20 -55 L-6 -10 L6 -10 L20 -55" fill="#121e36" stroke="#247bff" stroke-width="1.5"/>
      <rect x="-14" y="-12" width="28" height="14" rx="3" fill="#8b949e" stroke="#c9d1d9" stroke-width="1"/>
      <circle cx="0" cy="-5" r="3" fill="#070b16"/>
      <rect x="-8" y="2" width="16" height="8" rx="2" fill="#586069"/>

      <g style="transform-origin: 0px 0px; animation: lanyard-gentle-swing 6s ease-in-out infinite alternate;">
        <g transform="translate(-110, 12)">
          <rect x="0" y="0" width="220" height="330" rx="14" fill="url(#id-card-foil)" stroke="url(#id-border-grad)" stroke-width="1.8" style="filter: drop-shadow(0 12px 28px rgba(0,0,0,0.6));"/>
          
          <g clip-path="url(#id-badge-clip)">
            <rect x="-80" y="-80" width="120" height="480" fill="url(#id-shimmer-grad)" style="animation: foil-sweep 7s infinite ease-in-out;"/>

            <rect x="85" y="10" width="50" height="6" rx="3" fill="#070b16" stroke="#1f2d48" stroke-width="1"/>

            <text x="14" y="36" fill="#58a6ff" class="id-mono" font-size="9" font-weight="700" letter-spacing="1">DEV IDENTIFICATION</text>
            <circle cx="196" cy="33" r="5" fill="#00ff88"/>

            <g transform="translate(14, 46)" clip-path="url(#id-badge-photo-clip)">
              <rect width="192" height="150" fill="#080e1a"/>
              <image href="{id_b64}" x="-10" y="-15" width="210" height="180" preserveAspectRatio="xMidYMid slice"/>
              <rect width="192" height="150" rx="10" fill="none" stroke="#247bff" stroke-opacity="0.4" stroke-width="2"/>
            </g>

            <text x="14" y="218" fill="#ffffff" class="id-font" font-size="14" font-weight="800">DIVYANSH CHAUDHARY</text>
            <text x="14" y="234" fill="#58a6ff" class="id-mono" font-size="10.5" font-weight="600">AI / ML DEVELOPER</text>
            <text x="14" y="249" fill="#8b949e" class="id-font" font-size="10">ID: DC-2026-X88 · SONIPAT, IN</text>

            <!-- Barcode Pattern -->
            <g transform="translate(14, 264)">
              <rect x="0" y="0" width="192" height="32" rx="4" fill="#070c18" stroke="#16233a" stroke-width="0.8"/>
              <g transform="translate(12, 6)" fill="#c9d1d9">
                <rect x="0" y="0" width="3" height="20"/>
                <rect x="5" y="0" width="1" height="20"/>
                <rect x="8" y="0" width="4" height="20"/>
                <rect x="15" y="0" width="2" height="20"/>
                <rect x="19" y="0" width="1" height="20"/>
                <rect x="23" y="0" width="3" height="20"/>
                <rect x="29" y="0" width="2" height="20"/>
                <rect x="34" y="0" width="4" height="20"/>
                <rect x="41" y="0" width="1" height="20"/>
                <rect x="45" y="0" width="3" height="20"/>
                <rect x="51" y="0" width="2" height="20"/>
                <rect x="56" y="0" width="1" height="20"/>
                <rect x="60" y="0" width="4" height="20"/>
                <rect x="67" y="0" width="2" height="20"/>
                <rect x="72" y="0" width="3" height="20"/>
                <rect x="78" y="0" width="1" height="20"/>
                <rect x="82" y="0" width="3" height="20"/>
                <rect x="88" y="0" width="2" height="20"/>
                <rect x="93" y="0" width="4" height="20"/>
                <rect x="100" y="0" width="2" height="20"/>
                <rect x="105" y="0" width="1" height="20"/>
                <rect x="109" y="0" width="3" height="20"/>
                <rect x="115" y="0" width="4" height="20"/>
                <rect x="122" y="0" width="2" height="20"/>
                <rect x="127" y="0" width="1" height="20"/>
                <rect x="131" y="0" width="3" height="20"/>
                <rect x="137" y="0" width="4" height="20"/>
                <rect x="144" y="0" width="2" height="20"/>
                <rect x="149" y="0" width="3" height="20"/>
                <rect x="155" y="0" width="1" height="20"/>
                <rect x="159" y="0" width="3" height="20"/>
                <rect x="165" y="0" width="2" height="20"/>
              </g>
            </g>

            <text x="110" y="310" text-anchor="middle" fill="#586069" class="id-mono" font-size="8" letter-spacing="2">AUTHENTICATED PROFILE</text>
          </g>
        </g>
      </g>
    </g>

    <!-- RIGHT: VERIFIED METRICS DASHBOARD -->
    <g transform="translate(320, 68)">
      <rect width="518" height="330" rx="14" fill="#0b1322" stroke="#1a2742" stroke-width="1.2"/>

      <g transform="translate(24, 22)">
        <text x="0" y="14" fill="#ffffff" class="id-font" font-size="16" font-weight="800">SYSTEM TELEMETRY &amp; STATS</text>
        <rect x="370" y="0" width="100" height="22" rx="4" fill="#0f2620" stroke="#00ff88" stroke-opacity="0.5" stroke-width="1"/>
        <text x="380" y="15" fill="#00ff88" class="id-mono" font-size="10" font-weight="700">● VERIFIED</text>
      </g>

      <!-- Stat Cards Grid (2x2) -->
      <g transform="translate(24, 54)">
        <rect width="225" height="95" rx="10" fill="#080e1b" stroke="#247bff" stroke-opacity="0.5" stroke-width="1"/>
        <text x="16" y="24" fill="#8b949e" class="id-mono" font-size="10.5" font-weight="600">RYTH PLATFORM</text>
        <text x="16" y="60" fill="#ffffff" class="id-font" font-size="32" font-weight="900" letter-spacing="-0.5">200+</text>
        <text x="100" y="56" fill="#00ff88" class="id-mono" font-size="11" font-weight="700">USERS</text>
        <text x="16" y="82" fill="#58a6ff" class="id-font" font-size="11">Verified Active User Accounts</text>
      </g>

      <g transform="translate(269, 54)">
        <rect width="225" height="95" rx="10" fill="#080e1b" stroke="#ff354f" stroke-opacity="0.5" stroke-width="1"/>
        <text x="16" y="24" fill="#8b949e" class="id-mono" font-size="10.5" font-weight="600">DOMAIN SPEC</text>
        <text x="16" y="60" fill="#ffffff" class="id-font" font-size="28" font-weight="900">AI / ML</text>
        <text x="16" y="82" fill="#ff7b72" class="id-font" font-size="11">Neural Networks &amp; Pipelines</text>
      </g>

      <g transform="translate(24, 162)">
        <rect width="225" height="95" rx="10" fill="#080e1b" stroke="#1f2d48" stroke-width="1"/>
        <text x="16" y="24" fill="#8b949e" class="id-mono" font-size="10.5" font-weight="600">CORE TECHNOLOGIES</text>
        <text x="16" y="60" fill="#ffffff" class="id-font" font-size="32" font-weight="900">10+</text>
        <text x="80" y="56" fill="#58a6ff" class="id-mono" font-size="11" font-weight="700">TOOLS</text>
        <text x="16" y="82" fill="#8b949e" class="id-font" font-size="11">C++, Py, TF, React, Node.js</text>
      </g>

      <g transform="translate(269, 162)">
        <rect width="225" height="95" rx="10" fill="#080e1b" stroke="#1f2d48" stroke-width="1"/>
        <text x="16" y="24" fill="#8b949e" class="id-mono" font-size="10.5" font-weight="600">HANDLE // GITHUB</text>
        <text x="16" y="58" fill="#58a6ff" class="id-mono" font-size="18" font-weight="800">@divyansh-x</text>
        <text x="16" y="82" fill="#00ff88" class="id-font" font-size="11">Open Source &amp; Collaborations</text>
      </g>

      <g transform="translate(24, 272)">
        <rect width="470" height="38" rx="8" fill="#070c18" stroke="#1a2742" stroke-width="1"/>
        <circle cx="20" cy="19" r="4" fill="#00ff88"/>
        <text x="34" y="23" fill="#c9d1d9" class="id-font" font-size="11.5" font-weight="600">STATUS: Building autonomous AI systems &amp; high-scale platforms</text>
      </g>
    </g>

    <rect x="1" y="1" width="878" height="428" rx="15" fill="none" stroke="url(#id-border-grad)" stroke-width="1.5"/>
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
![Divyansh Chaudhary - Intro](./assets/hero.svg?v=3)

<!-- ABOUT & LIFE CAROUSEL -->
![About & Capabilities](./assets/about-life.svg?v=3)

<!-- TECH ARSENAL ORBIT -->
![System Tech Arsenal](./assets/stack.svg?v=3)

<!-- VERIFIED ID & TELEMETRY DASHBOARD -->
![Verified ID Dashboard](./assets/id-dashboard.svg?v=3)

<!-- CONNECT & COLLABORATE -->
![Let's Connect](./assets/connect.svg?v=3)

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
