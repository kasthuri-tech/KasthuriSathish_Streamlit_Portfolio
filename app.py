import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kasthuri Sathish | Senior Product Owner",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""<style>
    #MainMenu,footer,header,[data-testid="stHeader"]{display:none!important;}
    [data-testid="stAppViewContainer"]{padding-top:0;}
    .block-container{padding:0;max-width:100%;}
</style>""", unsafe_allow_html=True)

# ── Asset Loaders ───────────────────────────────────────────────────────────────
def load_image_b64(path, fallback):
    if os.path.exists(path):
        ext = "png" if path.endswith(".png") else "jpeg"
        with open(path, "rb") as f:
            return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode()}"
    return fallback

with open("assets/styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

profile_img_src = load_image_b64(
    "assets/profile.png",
    load_image_b64("assets/profile.jpg",
        "https://ui-avatars.com/api/?name=Kasthuri+Sathish&size=400&background=0a0a0a&color=00f2fe")
)
robot_img_src = load_image_b64(
    "assets/robot.jpg",
    "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600"
)

# ── Data ────────────────────────────────────────────────────────────────────────
NAV_LINKS = [
    ("Home", "#hero"), ("About", "#about"), ("Projects", "#projects"),
    ("Tech Stack", "#stack"), ("My Experience", "#my-experience"), ("Contact", "#contact"),
]

ABOUT_PARAGRAPHS = [
    "AI-Driven Senior Product Owner with 9+ years of experience leading end-to-end product delivery, Agile execution, and enterprise digital transformation initiatives across Healthcare, Financial Services, Automotive, and Travel domains.",
    "Experienced in stakeholder management, cross-functional team leadership, product delivery strategy, and data-driven decision-making using Agile methodologies. Passionate about building AI-powered solutions that improve operational efficiency, business intelligence, and user experience.",
    "Recently designed and developed an AI Financial Research Assistant using Python, Streamlit, Gemini API, Amazon Bedrock, Hugging Face deployment, semantic search, PDF/CSV intelligent data extraction, and interactive AI dashboards for financial research and insight generation.",
    "Focused on bridging business strategy with AI innovation to deliver scalable, impactful, and future-ready digital products.",
]

PROJECT_TAGS = ["Python","Streamlit","Gemini API","Amazon Bedrock","RAG","Hugging Face",
                "GitHub","Pandas","Sentence Transformers","PDF Analysis","Semantic Search",
                "Interactive Dashboard","AI-driven Insights"]

STACK_ITEMS = [
    ("☁️", "Streamlit Cloud",      "Interactive AI dashboard development and deployment platform."),
    ("🤗", "Hugging Face Spaces",  "AI application hosting and Generative AI solution deployment."),
    ("📊", "Power BI",             "Business intelligence and interactive analytics visualization platform."),
    ("✨", "Gemini API",           "Generative AI integration for intelligent AI-powered workflows."),
    ("🏗️","Amazon Bedrock",       "Enterprise GenAI experimentation and scalable AI integration."),
]

EXPERIENCE_SLIDES = [
    ("Senior Consultant",           "Capgemini",                      "Mar 2021 – Present | Bangalore"),
    ("Associate Consultant",        "Datamatics Global Services Ltd",  "May 2019 – Mar 2021 | Chennai"),
    ("Test Analyst",                "Stradegi Solutions",              "Jul 2018 – Apr 2019 | Chennai"),
    ("Software Test Engineer",      "Tekshapers Software Solutions",   "Feb 2018 – Jun 2018 | Chennai"),
    ("Associate Software Engineer", "Interglobe Technologies Pvt Ltd", "Jun 2015 – Apr 2017 | Chennai"),
]

CONTACT_DETAILS = [
    ("Email",     "kasthuri.vision@gmail.com", "mailto:kasthuri.vision@gmail.com", True),
    ("Phone",     "+91 8270747747",            None, False),
    ("Location",  "Tamil Nadu | Bangalore, India", None, False),
    ("Education", "Bachelor of Engineering",   None, False),
]

SOCIAL_LINKS = [
    ("GitHub",   "https://github.com/kasthuri-tech",        "https://simpleicons.org/icons/github.svg"),
    ("LinkedIn", "https://www.linkedin.com/in/kasthuri-vision", "https://simpleicons.org/icons/linkedin.svg"),
]

# ── HTML Builders ───────────────────────────────────────────────────────────────
def build_nav():
    parts = []
    for label, href in NAV_LINKS:
        active = ' class="active"' if label == "Home" else ""
        parts.append(f'<li><a href="{href}"{active}>{label}</a></li>')
    items = "\n".join(parts)
    return f'<nav class="navbar" style="pointer-events:auto;"><ul class="nav-links">{items}</ul></nav>'

def build_tags(tags):
    return "\n".join(f'<span class="tag">{t}</span>' for t in tags)

def build_stack_cards():
    delays = ["delay-1","delay-2","delay-3","delay-1","delay-2"]
    return "\n".join(
        f'''<div class="stack-card glass-panel fade-in {delays[i]}" data-tilt data-tilt-scale="1.02">
              <div class="stack-icon">{icon}</div>
              <div class="stack-content">
                <h3 class="stack-title">{title}</h3>
                <p class="stack-desc"><span style="color:var(--accent-teal);font-weight:600;">Capabilities:</span> {desc}</p>
              </div>
            </div>'''
        for i, (icon, title, desc) in enumerate(STACK_ITEMS)
    )

def build_experience_slides():
    return "\n".join(
        f'''<div class="slide-card glass-panel">
              <h4>{role}</h4>
              <p class="company">{company}</p>
              <p class="duration">{duration}</p>
            </div>'''
        for role, company, duration in EXPERIENCE_SLIDES
    )

def build_contact_details():
    rows = []
    for label, value, href, is_link in CONTACT_DETAILS:
        val_html = f'<a href="{href}" class="detail-value">{value}</a>' if is_link else f'<p class="detail-value">{value}</p>'
        rows.append(f'<div class="detail-item"><p class="detail-label">{label}</p>{val_html}</div>')
    return "\n".join(rows)

def build_footer_social_icons():
    return "\n".join(
        f'<a href="{url}" target="_blank" class="footer-social-icon"><img src="{icon}" alt="{name}"/></a>'
        for name, url, icon in SOCIAL_LINKS
    )

def build_footer_text_links():
    return "\n".join(
        f'<a href="{url}" target="_blank" class="footer-text-link">{name} ↗</a>'
        for name, url, _ in SOCIAL_LINKS
    )

# ── Page Assembly ───────────────────────────────────────────────────────────────
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Kasthuri Sathish - AI Product Owner</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Outfit:wght@400;700;900&display=swap" rel="stylesheet"/>
  <style>
    {css_content}
    body{{margin:0;padding:0;width:100%;height:100%;}}
    .skillset-typed{{font-size:1.1rem;color:var(--accent-teal);margin-bottom:2rem;display:block;}}
  </style>
  <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
  <script src="https://cdn.jsdelivr.net/npm/vanilla-tilt@1.7.2/dist/vanilla-tilt.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/tsparticles@2.11.0/tsparticles.bundle.min.js"></script>
</head>
<body>

  <div class="custom-cursor" id="custom-cursor"></div>
  <div id="tsparticles" style="position:fixed;width:100%;height:100%;z-index:0;pointer-events:none;"></div>

  {build_nav()}

  <!-- HERO -->
  <section id="hero" class="hero section fade-in" style="z-index:10;position:relative;">
    <div class="hero-left">
      <h1 class="hero-name">Kasthuri<br/>Sathish</h1>
      <h3 class="hero-title" style="margin-bottom:.5rem;">SENIOR PRODUCT OWNER</h3>
      <h2 class="hero-subtitle" style="margin-bottom:.5rem;">9+ Years Experience</h2>
      <div class="skillset-typed"><span id="typed"></span></div>
      <div class="domains" style="color:var(--text-muted);font-size:.95rem;letter-spacing:1px;margin-bottom:2rem;">
        | Healthcare | Financial Services | Automotive | Travel |
      </div>
      <div class="hero-social-buttons">
        <a href="https://github.com/kasthuri-tech" target="_blank" class="hero-social-btn">
          <img src="https://simpleicons.org/icons/github.svg" alt="GitHub"/> GitHub
        </a>
        <a href="https://www.linkedin.com/in/kasthuri-vision" target="_blank" class="hero-social-btn">
          <img src="https://simpleicons.org/icons/linkedin.svg" alt="LinkedIn"/> LinkedIn
        </a>
      </div>
    </div>
    <div class="hero-right">
      <div class="profile-container">
        <div class="profile-glow-ring"></div>
        <div class="profile-img-wrapper">
          <img src="{profile_img_src}" alt="Kasthuri Sathish" class="profile-img"/>
        </div>
      </div>
    </div>
  </section>

  <!-- ABOUT -->
  <section id="about" class="about-section section fade-in">
    <div class="about-left">
      <h2 class="section-heading" style="text-align:left;margin-bottom:1.5rem;font-size:2.5rem;">About Me</h2>
      {"".join(f'<p class="about-text">{p}</p>' for p in ABOUT_PARAGRAPHS)}
    </div>
  </section>

  <!-- PROJECTS -->
  <section id="dashboard" class="dashboard-section section">
    <div class="dashboard-grid">
      <div class="glass-panel fade-in delay-1" data-tilt data-tilt-scale="1.02" id="projects" style="grid-column:1/-1;">
        <div class="card-icon">🚀</div>
        <h3 class="card-title">Projects</h3>
        <div class="card-content">
          <p style="font-weight:600;color:#fff;margin-bottom:.5rem;">AI Financial Research Assistant</p>
          <p>AI-powered financial research platform designed for intelligent financial analysis, semantic search, document summarization, and interactive investment insights using modern Generative AI technologies.</p>
          <div class="tag-container">{build_tags(PROJECT_TAGS)}</div>
        </div>
      </div>
    </div>

    <!-- MY EXPERIENCE SLIDER -->
    <div id="my-experience" class="slider-container fade-in delay-3" style="margin-top:5rem;">
      <h2 class="section-heading" style="text-align:left;margin-bottom:1.5rem;font-size:2.2rem;padding-left:10px;">My Experience</h2>
      <button class="slider-btn left" id="slideLeft">❮</button>
      <div class="slider-track" id="sliderTrack">
        {build_experience_slides()}
      </div>
      <button class="slider-btn right" id="slideRight">❯</button>
    </div>
  </section>

  <!-- AI STACK -->
  <section id="stack" class="section">
    <h2 class="section-heading fade-in delay-1" style="margin-bottom:3rem;">AI Solutions &amp; Deployment Stack</h2>
    <div class="stack-container">
      {build_stack_cards()}
    </div>
  </section>

  <!-- CONTACT FOOTER -->
  <footer id="contact" class="footer-section fade-in delay-2">
    <h2 class="section-heading" style="text-align:left;margin-bottom:3rem;font-size:2.2rem;">CONTACT</h2>
    <div class="footer-grid">
      <div class="footer-col col-socials">{build_footer_social_icons()}</div>
      <div class="footer-col col-details">{build_contact_details()}</div>
      <div class="footer-col col-links">{build_footer_text_links()}</div>
      <div class="footer-col col-branding">
        <p class="brand-text">Designed and Developed by<br/><span class="brand-name">Kasthuri Sathish</span></p>
        <p class="brand-copyright">© 2026</p>
      </div>
    </div>
    <a href="#hero" class="resume-btn">RESUME 📄</a>
  </footer>

  <script>
    document.addEventListener("DOMContentLoaded", function() {{

      // Particles
      if(typeof tsParticles !== 'undefined') {{
        tsParticles.load("tsparticles", {{
          fullScreen: {{enable: false}},
          background: {{color: {{value: "transparent"}}}},
          particles: {{
            number: {{value: 60, density: {{enable: true, value_area: 800}}}},
            color: {{value: ["#00f2fe","#4facfe","#ffffff"]}},
            shape: {{type: "circle"}},
            opacity: {{value: 0.5, random: true}},
            size: {{value: 3, random: true}},
            line_linked: {{enable: true, distance: 150, color: "#4facfe", opacity: 0.2, width: 1}},
            move: {{enable: true, speed: 1, direction: "none", random: true, out_mode: "out"}}
          }},
          interactivity: {{
            detect_on: "window",
            events: {{onhover: {{enable: true, mode: "grab"}}, onclick: {{enable: true, mode: "push"}}}},
            modes: {{grab: {{distance: 200, line_linked: {{opacity: 0.5}}}}, push: {{particles_nb: 3}}}}
          }},
          retina_detect: true
        }});
      }}

      // Typed.js
      if(document.getElementById('typed')) {{
        new Typed('#typed', {{
          strings: ["Cross-Functional Leadership"],
          typeSpeed: 40, backSpeed: 30, backDelay: 2000, loop: true, showCursor: true, cursorChar: '|'
        }});
      }}

      // Vanilla Tilt
      if(typeof VanillaTilt !== 'undefined') {{
        VanillaTilt.init(document.querySelectorAll("[data-tilt]"));
      }}

      // Nav scroll-spy with click-lock
      const sections = document.querySelectorAll("section, .slider-container");
      const navLinks = document.querySelectorAll(".nav-links li a");
      let navLocked = false;

      document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
        anchor.addEventListener('click', function(e) {{
          e.preventDefault();
          const id = this.getAttribute('href');
          const target = document.querySelector(id);
          if (!target) return;
          const isCard = target.classList.contains('glass-panel') || target.classList.contains('slider-container');
          target.scrollIntoView({{behavior: 'smooth', block: isCard ? 'center' : 'start'}});
          if (target.classList.contains('glass-panel')) {{
            target.classList.remove('highlight-anim');
            void target.offsetWidth;
            target.classList.add('highlight-anim');
          }}
          navLinks.forEach(l => l.classList.remove('active'));
          const clicked = document.querySelector(`.nav-links a[href="${{id}}"]`);
          if (clicked) clicked.classList.add('active');
          navLocked = true;
          setTimeout(() => {{ navLocked = false; }}, 1200);
        }});
      }});

      document.addEventListener("scroll", () => {{
        if (navLocked) return;
        let current = "";
        sections.forEach(s => {{ if (window.scrollY >= s.offsetTop - 250) current = s.getAttribute("id"); }});
        navLinks.forEach(l => {{
          l.classList.remove("active");
          if (current && l.getAttribute("href") === "#" + current) l.classList.add("active");
        }});
      }});

      // Custom Cursor
      const cursor = document.getElementById("custom-cursor");
      document.addEventListener("mousemove", e => {{ cursor.style.left = e.clientX+"px"; cursor.style.top = e.clientY+"px"; }});
      document.querySelectorAll("a,button,.glass-panel,.hero-social-btn").forEach(el => {{
        el.addEventListener("mouseenter", () => cursor.classList.add("hover"));
        el.addEventListener("mouseleave", () => cursor.classList.remove("hover"));
      }});

      // Slider
      const track = document.getElementById('sliderTrack');
      const slides = document.querySelectorAll('.slide-card');
      let cur = 0;
      const updateSlider = () => {{
        track.style.transform = `translateX(-${{cur * (slides[0].offsetWidth + 32)}}px)`;
      }};
      document.getElementById('slideRight').addEventListener('click', () => {{ if(cur < slides.length-1) {{ cur++; updateSlider(); }} }});
      document.getElementById('slideLeft').addEventListener('click',  () => {{ if(cur > 0) {{ cur--; updateSlider(); }} }});

      // Scroll-reveal
      const observer = new IntersectionObserver(entries => {{
        entries.forEach(e => {{ if(e.isIntersecting) {{ e.target.classList.add('visible'); observer.unobserve(e.target); }} }});
      }}, {{threshold: 0.1}});
      document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
    }});
  </script>
</body>
</html>"""

components.html(html_content, height=2000, scrolling=True)
