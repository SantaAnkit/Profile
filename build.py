\
import os

ICONS = {
"mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
"file": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/></svg>',
"scholar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.1 2.7 3 6 3s6-1.9 6-3v-5"/></svg>',
"github": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/></svg>',
"linkedin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4V8h4v1.5A6 6 0 0 1 16 8Z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="1.5"/></svg>',
}

PAGES = [
    ("index",        "Home",                       "index.html"),
    ("research",      "Research interests",         "research.html"),
    ("publications",  "Publications & Achievements", "publications.html"),
    ("teaching",       "Teaching",                   "teaching.html"),
    ("education",      "Education",                  "education.html"),
    ("activities",     "Activities",                 "activities.html"),
]

def sidebar(active_key):
    links = "\n      ".join(
        f'<a href="{href}"{" class=\"active\"" if key==active_key else ""}>{label}</a>'
        for key, label, href in PAGES
    )
    return f"""  <aside class="sidebar">
    <img class="portrait" src="Images/IMG20250414104531.jpg" alt="Portrait of Ankit" />
    <h1 class="name">Ankit</h1>
    <p class="role">PhD Research Scholar, Mehta Family School of Data Science and Artificial Intelligence, Department of Data Science</p>
    <p class="location">📍 IIT Palakkad, Kerala, India</p>

    <div class="social-icons">
      <a class="icon-btn" href="mailto:142214001@smail.iitpkd.ac.in" aria-label="Email" title="Email">{ICONS['mail']}</a>
      <a class="icon-btn" href="CV.pdf" aria-label="CV" title="CV">{ICONS['file']}</a>
      <a class="icon-btn" href="https://scholar.google.com/citations?user=SnmEbEMAAAAJ&hl=en" target="_blank" rel="noopener" aria-label="Google Scholar" title="Google Scholar">{ICONS['scholar']}</a>
      <a class="icon-btn" href="https://github.com/santaankit" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub">{ICONS['github']}</a>
      <a class="icon-btn" href="https://www.linkedin.com/in/ankit-santa-909a9b238/" target="_blank" rel="noopener" aria-label="LinkedIn" title="LinkedIn">{ICONS['linkedin']}</a>
    </div>

    <nav class="section-nav">
      {links}
    </nav>
  </aside>"""

def page(active_key, title, content, extra_class=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Ankit — {title}</title>
<meta name="description" content="Ankit — PhD Research Scholar, Data Science, IIT Palakkad. {title}." />

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css" />
</head>
<body>
<div class="page">
{sidebar(active_key)}
  <main class="content{(' ' + extra_class) if extra_class else ''}">
{content}
    <footer class="footer">
      <p>© <span id="year"></span> Ankit · PhD Research Scholar in Data Science · IIT Palakkad · All rights reserved</p>
    </footer>
  </main>
</div>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

# ---------------- HOME ----------------
home_content = """    <section class="hero">
      <div class="hero-grid">
        <img src="Images/DSC_0105.jpg" alt="" />
        <img src="Images/IMG_20260429_122300.jpg" alt="" />
        <img src="Images/IMG_0455.JPG" alt="" />
        <img src="Images/_SON8055.JPG" alt="" />
      </div>
    </section>

    <section id="bio" class="section first">
      <h2>Hello!</h2>
      <p>
        I'm a PhD research student at IIT Palakkad, working in the area of bioinformatics and
        computational drug discovery.
      </p>
    </section>"""

# ---------------- RESEARCH ----------------
research_content = """    <section id="research" class="section first">
      <h2>Research interests</h2>
      <p>
        My research focuses on using 3D molecular structures to develop machine learning models
        for drug design, with a particular interest in making 3D graph-based models more
        explainable and easier to understand.
      </p>
      <ul class="tag-list">
        <li>3D Graph Kernels</li>
        <li>3D Graph Neural Networks</li>
        <li>XAI</li>
        <li>Graph Machine Learning</li>
      </ul>
    </section>"""

# ---------------- PUBLICATIONS & ACHIEVEMENTS ----------------
pub_content = """    <section id="publications" class="section first">
      <h2>Publications</h2>

      <article class="pub">
        <h3 class="pub-title"><a href="https://academic.oup.com/bioinformatics/article/41/Supplement_1/i58/8199352" target="_blank" rel="noopener">Efficient 3D kernels for molecular property prediction</a></h3>
        <p class="pub-authors"><strong>Ankit</strong>, Sahely Bhadra, Juho Rousu</p>
        <p class="pub-venue">ISMB/ECCB 2025</p>
        <p class="pub-links">
          <a href="https://academic.oup.com/bioinformatics/article/41/Supplement_1/i58/8199352" target="_blank" rel="noopener">Paper</a> ·
          <a href="https://github.com/SantaAnkit/Efficient-3D-kernels-for-molecular-property-prediction" target="_blank" rel="noopener">Code</a>
        </p>
      </article>

      <p class="hint">Add more publications by duplicating the block above in publications.html.</p>
    </section>

    <section id="achievements" class="section">
      <h2>Achievements</h2>

      <div class="timeline-item">
        <p class="timeline-meta">2026</p>
        <h3 class="timeline-title">Cricket General Championship — IIT Palakkad</h3>
        <p class="timeline-org">Won the Cricket General Championship representing the institute.</p>
      </div>

      <p class="hint">Add more awards, honours, or championships here — duplicate the block above in publications.html.</p>
    </section>"""

# ---------------- TEACHING ----------------
teaching_entries = [
    ("Fall 2023", "Optimization (DS-2010)", "Assisted with tutorials, student queries, assignments, and course activities."),
    ("Spring 2024", "Responsible Artificial Intelligence (DS-5604)", "Assisted students with course concepts, assignments, and academic activities."),
    ("Fall 2024", "Introduction to Machine Learning (DS-3010)", "Assisted students with machine learning concepts, assignments, and course activities."),
    ("Spring 2025", "Introduction to Deep Learning (DS-3040)", "Assisted students with deep learning concepts, assignments, and course activities."),
    ("Fall 2025", "Introduction to Machine Learning (DS-3010)", "Assisted students with machine learning concepts, assignments, and course activities."),
    ("Spring 2026", "Deep Learning (DS-5007)", "Assisted students with deep learning concepts, assignments, and course activities."),
    ("Fall 2026", "Data Structures and Algorithms for Data Science (DS-2030)", "Assisting students with data structures, algorithms, assignments, and course activities in Python."),
]
teaching_items = "\n\n".join(f"""      <div class="timeline-item">
        <p class="timeline-meta">{term}</p>
        <h3 class="timeline-title">Teaching Assistant — {course}</h3>
        <p class="timeline-org">Department of Data Science, IIT Palakkad</p>
        <p>{desc}</p>
      </div>""" for term, course, desc in teaching_entries)
teaching_content = f"""    <section id="teaching" class="section first">
      <h2>Teaching</h2>
{teaching_items}
    </section>"""

# ---------------- EDUCATION ----------------
edu_entries = [
    ("2022 — present", "PhD in Data Science", "Indian Institute of Technology Palakkad"),
    ("2021 — 2022", "M.Phil. in Mathematics", "Himachal Pradesh University, Shimla, Himachal Pradesh"),
    ("2018 — 2020", "M.Sc. in Mathematics", "Himachal Pradesh University, Shimla, Himachal Pradesh"),
    ("2015 — 2018", "B.Sc. Hons. in Mathematics", "Government Degree College Sanjauli, Shimla, Himachal Pradesh"),
]
edu_items = "\n\n".join(f"""      <div class="timeline-item">
        <p class="timeline-meta">{term}</p>
        <h3 class="timeline-title">{degree}</h3>
        <p class="timeline-org">{org}</p>
      </div>""" for term, degree, org in edu_entries)
education_content = f"""    <section id="education" class="section first">
      <h2>Education</h2>
{edu_items}
    </section>"""

# ---------------- ACTIVITIES ----------------
activities_content = """    <section id="activities" class="section first">
      <h2>Other activities</h2>
      <p>
        Outside of research, I enjoy playing different kinds of games and spending time on
        things that help me take a break from my work. Cricket is one of my favorite games,
        and I especially enjoy playing it whenever I get the chance.
      </p>

      <div class="gallery">
        <figure class="gallery-item span-2">
          <img src="Images/DSC_0105.jpg" alt="Participating in the toss before a cricket match at the Inter-IIT Sports Meet" />
        </figure>
        <figure class="gallery-item">
          <img src="Images/IMG_20260429_122300.jpg" alt="Receiving the winning certificate after securing the Cricket General Championship at IIT Palakkad" />
        </figure>
        <figure class="gallery-item">
          <img src="Images/IMG_0455.JPG" alt="Poster presentation at IIT Palakkad" />
        </figure>
        <figure class="gallery-item span-2">
          <img src="Images/_SON8055.JPG" alt="Giving a research talk during Research Scholar Day at IIT Palakkad" />
        </figure>
      </div>
    </section>"""

files = {
    "index.html": page("index", "Home", home_content),
    "research.html": page("research", "Research interests", research_content),
    "publications.html": page("publications", "Publications & Achievements", pub_content),
    "teaching.html": page("teaching", "Teaching", teaching_content),
    "education.html": page("education", "Education", education_content),
    "activities.html": page("activities", "Activities", activities_content, extra_class="activities-page"),
}

for name, html in files.items():
    with open(name, "w") as f:
        f.write(html)

print("Generated:", ", ".join(files.keys()))
