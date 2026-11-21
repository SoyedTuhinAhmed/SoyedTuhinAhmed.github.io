"""Build index.html and publications.html from the templates in _src/.

Usage (from the repository root):  python3 _src/build.py

To add a paper: append a tuple to P below (and its abstract to abstracts.json if you
want an Abstract button), add its id to SELECTED to feature it on the home page,
put the PDF in assets/papers/, then re-run this script.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
import html, json

ME = "Soyed Tuhin Ahmed"
MENTEES = {"Fahim Ul Islam", "Pragya Sharma", "Surendra Hemaram", "Roman Rakhmatullin"}
TDA = ["Soyed Tuhin Ahmed", "Kamal Danouchi", "Michael Hefenbrock", "Guillaume Prenat", "Lorena Anghel", "Mehdi B. Tahoori"]
SANDIA = ["Soyed Tuhin Ahmed", "Eduardo Ortega", "Ryan Dempsey", "Patrick Xiao", "Ben Feinberg", "Christopher H. Bennett", "Matthew J. Marinella", "Krishnendu Chakrabarty"]

# id, type(journal/conference/review/preprint/forum), badge, year, title, authors, venue, award, pdf, doi
P = [
 ("J1","journal","TCAD",2026,"HARD-DPO: Hardware-Aware Robust Direct Preference Optimization for RRAM-based LLM Accelerators",[ME,"Krishnendu Chakrabarty"],"IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), accepted, 2026","", "HARD-DPO_TCAD2026.pdf",""),
 ("J2","journal","TETC",2026,"Concurrent Self-Testing and Uncertainty Estimation of Neural Networks Using Uncertainty Fingerprint",[ME,"Mehdi B. Tahoori"],"IEEE Transactions on Emerging Topics in Computing (TETC), vol. 14, no. 1, pp. 118–133, 2026","","",""),
 ("J3","journal","TCAD",2026,"Scale-Dropout: Estimating Uncertainty in Deep Neural Networks Using Stochastic Scale",TDA,"IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), vol. 45, no. 7, pp. 3113–3128, 2026","","",""),
 ("J4","journal","JETCAS",2025,"MoF-LoRA: Mixture of Low-Rank Fault-Tolerant Experts for RRAM-based In-Memory Computing",SANDIA,"IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), 2025","2026 Spotlight Paper","MoF-LoRA_JETCAS2026.pdf","10.1109/JETCAS.2026.3655242"),
 ("J5","journal","TCAD",2024,"One-Shot Online Testing of Deep Neural Networks Based on Distribution Shift Detection",[ME,"Mehdi B. Tahoori"],"IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2024","","",""),
 ("J6","journal","TNANO",2023,"Spatial-SpinDrop: Spatial Dropout-Based Binary Bayesian Neural Network with Spintronics Implementation",TDA,"IEEE Transactions on Nanotechnology (TNANO), 2023","","",""),
 ("J7","journal","TECS",2023,"SpinBayes: Algorithm-Hardware Co-Design for Uncertainty Estimation Using Bayesian In-Memory Approximation on Spintronic-Based Architectures",TDA,"ACM Transactions on Embedded Computing Systems (TECS, ESWEEK special issue), 2023","","",""),
 ("J8","journal","JETC",2023,"Design-Time Reference Current Generation for Robust Spintronic-Based Neuromorphic Architecture",[ME,"Mahta Mayahinia","Michael Hefenbrock","Christopher Münch","Mehdi B. Tahoori"],"ACM Journal on Emerging Technologies in Computing Systems (JETC), vol. 20, no. 1, pp. 1–20, 2023","","",""),
 ("J9","journal","D&amp;T",2023,"Fault-Tolerant Neuromorphic Computing with Memristors Using Functional ATPG for Efficient Re-calibration",[ME,"Mehdi B. Tahoori"],"IEEE Design &amp; Test, 2023","Invited: Top Picks of VTS 2022","",""),
 ("J10","journal","JETCAS",2023,"SpinDrop: Dropout-Based Bayesian Binary Neural Networks with Spintronic Implementation",[ME,"Kamal Danouchi","Christopher Münch","Guillaume Prenat","Lorena Anghel","Mehdi B. Tahoori"],"IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), vol. 13, no. 1, pp. 150–164, 2023","JETCAS Best Paper Award 2024","SpinDrop_JETCAS2023.pdf","10.1109/JETCAS.2023.3242146"),
 ("J11","journal","TCAD",2023,"NeuroScrub+: Mitigating Retention Faults Using Flexible Approximate Scrubbing in Neuromorphic Fabric Based on Resistive Memories",[ME,"Michael Hefenbrock","Christopher Münch","Mehdi B. Tahoori"],"IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), vol. 42, no. 5, pp. 1490–1503, 2023","","",""),

 ("C1","conference","FPT",2026,"Architecting Resilient and Secure Space Data Centers",["Pragya Sharma","Ashish Reddy Bommana",ME,"Bahar Farahani","Krishnendu Chakrabarty","Farshad Firouzi"],"International Conference on Field-Programmable Technology (FPT), 2026","","",""),
 ("C2","conference","ITC",2026,"CREW: Collapse-Resilient Generative Augmentation for Wafer Defect Classification",["Fahim Ul Islam",ME,"John Carulli","Krishnendu Chakrabarty"],"IEEE International Test Conference (ITC), 2026","","",""),
 ("C3","conference","COINS",2026,"Space Data Centers (SDCs): Rethinking Computing Infrastructure Beyond Earth",[ME,"Bahar Farahani","Krishnendu Chakrabarty","Farshad Firouzi"],"IEEE International Conference on Omni-Layer Intelligent Systems (COINS), 2026","","SpaceDataCenters_COINS2026.pdf","10.1109/COINS69995.2026.11715566"),
 ("C4","conference","ETS",2026,"Reliability, Test, and Security of Compute-In-Memories",[ME,"Krishnendu Chakrabarty","Jin-Fu Li","Mottaqiallah Taouil","Fouwad Jamil Mir","Said Hamdioui","Mehdi B. Tahoori","Martin Keim","Jongsin Yun"],"IEEE European Test Symposium (ETS), 2026","Special-session paper","",""),
 ("C5","conference","VTS",2026,"The Fracture Bits in Large Language Models",[ME,"Farshad Firouzi","Krishnendu Chakrabarty"],"IEEE VLSI Test Symposium (VTS), 2026","","",""),
 ("C6","conference","VTS",2026,"MoD-CiM: A Mixture-of-Defenses Framework Against Power-Hammering Attacks in Multi-Tenant Compute-in-Memory",["Ashish Reddy Bommana",ME,"Farshad Firouzi","Krishnendu Chakrabarty"],"IEEE VLSI Test Symposium (VTS), 2026","","MoD-CiM_VTS2026.pdf","10.1109/VTS69484.2026.11563202"),
 ("C7","conference","VTS",2026,"HAT-FI: Hardware-Aware Training for Fault-Tolerant LLM Inference on RRAM-Based Compute-in-Memory",["Pragya Sharma",ME,"Farshad Firouzi","Krishnendu Chakrabarty"],"IEEE VLSI Test Symposium (VTS), 2026","","",""),
 ("C8","conference","VTS",2026,"DefectVICL: Data-Efficient Wafer Defect Classification with Vision In-Context Learning",["Fahim Ul Islam",ME,"John Carulli","Krishnendu Chakrabarty"],"44th IEEE VLSI Test Symposium (VTS), 2026","","",""),
 ("C9","conference","ITC",2025,"Fault Tolerance in RRAM-based AI Accelerator with Guided Randomized Activation",SANDIA,"IEEE International Test Conference (ITC), 2025","","GuidedRandomizedActivation_ITC2025.pdf","10.1109/ITC58126.2025.00039"),
 ("C10","conference","ICCAD",2024,"Tiny Deep Ensemble: Uncertainty Estimation in Edge AI Accelerators via Ensembling Normalization Layers with Shared Weights",[ME,"Mehdi B. Tahoori"],"ACM/IEEE International Conference on Computer-Aided Design (ICCAD), 2024","","TinyDeepEnsemble_ICCAD2024.pdf","10.1145/3676536.3676804"),
 ("C11","conference","DATE",2024,"NeuSpin: Design of a Reliable Edge Neuromorphic System Based on Spintronics for Green AI",[ME,"Kamal Danouchi","Guillaume Prenat","Lorena Anghel","Mehdi B. Tahoori"],"Design, Automation and Test in Europe Conference (DATE), 2024","","",""),
 ("C12","conference","ETS",2024,"Testing Spintronics-Implemented Monte Carlo Dropout-Based Bayesian Neural Networks",TDA,"IEEE European Test Symposium (ETS), 2024","","",""),
 ("C13","conference","DATE",2024,"Enhancing Reliability of Neural Networks at the Edge: Inverted Normalization with Stochastic Affine Transformations",TDA,"Design, Automation and Test in Europe Conference (DATE), 2024","Best Paper Nominee","",""),
 ("C14","conference","VTS",2024,"NN-ECC: Embedding Error Correction Codes in Neural Network Weight Memories Using Multi-task Learning",[ME,"Surendra Hemaram","Mehdi B. Tahoori"],"42nd IEEE VLSI Test Symposium (VTS), 2024","VTS 2024 Best Paper Award","",""),
 ("C15","conference","VTS",2023,"A Low Overhead Checksum Technique for Error Correction in Memristive Crossbar for Deep Learning Applications",["Surendra Hemaram",ME,"Mahta Mayahinia","Christopher Münch","Mehdi B. Tahoori"],"41st IEEE VLSI Test Symposium (VTS), 2023","","",""),
 ("C16","conference","DATE",2023,"Scalable Spintronics-Based Bayesian Neural Network for Uncertainty Estimation",TDA,"Design, Automation and Test in Europe Conference (DATE), 2023","","",""),
 ("C17","conference","ETS",2023,"Online Fault-Tolerance for Memristive Neuromorphic Fabric Based on Local Approximation",[ME,"Roman Rakhmatullin","Mehdi B. Tahoori"],"28th IEEE European Test Symposium (ETS), 2023","","",""),
 ("C18","conference","DSD",2022,"MVSTT: A Multi-Value Computation-in-Memory Based on Spin-Transfer Torque Memories",["Atousa Jafari","Mahta Mayahinia",ME,"Christopher Münch","Mehdi B. Tahoori"],"25th Euromicro Conference on Digital System Design (DSD), 2022","","",""),
 ("C19","conference","VTS",2022,"Fault-Tolerant Neuromorphic Computing with Functional ATPG for Post-Manufacturing Re-calibration",[ME,"Mehdi B. Tahoori"],"40th IEEE VLSI Test Symposium (VTS), 2022","Best Paper Nominee","",""),
 ("C20","conference","ETS",2022,"Process and Runtime Variation Robustness for Spintronic-Based Neuromorphic Fabric",[ME,"Mahta Mayahinia","Michael Hefenbrock","Christopher Münch","Mehdi B. Tahoori"],"IEEE European Test Symposium (ETS), 2022","","",""),
 ("C21","conference","ITC",2022,"Compact Functional Test Generation for Memristive Deep Learning Implementations Using Approximate Gradient Ranking",[ME,"Mehdi B. Tahoori"],"IEEE International Test Conference (ITC), 2022","","",""),
 ("C22","conference","NANOARCH",2022,"Binary Bayesian Neural Networks for Efficient Uncertainty Estimation Leveraging Inherent Stochasticity of Spintronic Devices",TDA,"IEEE/ACM International Symposium on Nanoscale Architectures (NANOARCH), 2022","Best Paper Nominee","",""),
 ("C23","conference","ETS",2021,"NeuroScrub: Mitigating Retention Failures Using Approximate Scrubbing in Neuromorphic Fabric Based on Resistive Memories",[ME,"Michael Hefenbrock","Christopher Münch","Mehdi B. Tahoori"],"IEEE European Test Symposium (ETS), 2021","","",""),

 ("R1","preprint","arXiv",2024,"Few-Shot Testing: Estimating Uncertainty of Memristive Deep Neural Networks Using One Bayesian Test Vector",[ME,"Mehdi B. Tahoori"],"arXiv:2405.18894, 2024","","",""),
 ("P1","forum","DATE",2024,"Scalable and Efficient Methods for Uncertainty Estimation and Reduction in Deep Learning",[ME],"PhD Forum, Design, Automation and Test in Europe Conference (DATE), 2024","","",""),
 ("P2","forum","ESWEEK",2023,"Scalable Uncertainty Estimation Approaches in Memristive Deep Learning",[ME],"PhD Forum, Embedded Systems Week (ESWEEK), 2023","","",""),
 ("P3","forum","DATE",2023,"Reliable Memristive Neuromorphic In-Memory Computing: An Algorithm-Hardware Co-Design Approach",[ME],"PhD Forum, Design, Automation and Test in Europe Conference (DATE), 2023","","",""),
]

ABS = json.load(open(os.path.join(HERE, "abstracts.json"), encoding="utf-8"))  # id -> abstract
ARXIV = {"R1": "https://arxiv.org/abs/2405.18894"}

def authors(lst):
    out = []
    for a in lst:
        e = html.escape(a)
        if a == ME: e = f'<span class="me">{e}</span>'
        elif a in MENTEES: e = f'<span class="mentee">{e}</span>'
        out.append(e)
    return ", ".join(out)

def badge_cls(t):
    return {"journal": "", "conference": "conf"}.get(t, "ur")

def render(p, prefix="", show_id=True):
    pid, t, badge, yr, title, au, venue, award, pdf, doi = p
    first = "1" if au[0] == ME else "0"
    award_html = f' <span class="award-tag"><i class="fa-solid fa-award"></i> {award}</span>' if award else ""
    acts = []
    if pid in ABS: acts.append(f'<button type="button" data-abs="{prefix}abs-{pid}">Abstract</button>')
    if pdf: acts.append(f'<a href="assets/papers/{pdf}" target="_blank" rel="noopener"><i class="fa-regular fa-file-pdf"></i> PDF</a>')
    if doi: acts.append(f'<a href="https://doi.org/{doi}" target="_blank" rel="noopener">DOI</a>')
    if pid in ARXIV: acts.append(f'<a href="{ARXIV[pid]}" target="_blank" rel="noopener">arXiv</a>')
    acts_html = f'<div class="pub-actions">{"".join(acts)}</div>' if acts else ""
    abs_html = f'<div class="abstract" id="{prefix}abs-{pid}">{html.escape(ABS[pid])}</div>' if pid in ABS else ""
    idtxt = f'<small>[{pid}]</small>' if show_id else f'<small>{yr}</small>'
    return f'''<article class="pub" data-type="{t}" data-first="{first}">
  <div class="venue-badge {badge_cls(t)}">{badge}{idtxt}</div>
  <div>
    <div class="title">{html.escape(title)}</div>
    <div class="authors">{authors(au)}</div>
    <div class="where">{venue}{award_html}</div>
    {acts_html}
    {abs_html}
  </div>
</article>'''

SELECTED = ["J1", "J4", "C5", "C9", "C3", "C6", "C10", "J10", "C14"]
byid = {p[0]: p for p in P}
sel = "\n".join(render(byid[i], prefix="s-", show_id=False) for i in SELECTED)

groups = []
for yr in sorted({p[3] for p in P}, reverse=True):
    items = [p for p in P if p[3] == yr]
    order = {"journal": 0, "conference": 1, "preprint": 2, "forum": 3}
    items.sort(key=lambda p: (order[p[1]], int(p[0][1:])))
    groups.append(f'<div class="year-group"><h3 class="year-head">{yr}</h3>\n' + "\n".join(render(p) for p in items) + '\n</div>')
full = "\n".join(groups)

# Structured data (schema.org) so search engines understand each paper and its authors
SITE = "https://soyedtuhinahmed.github.io/"
def article(p):
    pid, t, badge, yr, title, au, venue, award, pdf, doi = p
    a = {
        "@type": "ScholarlyArticle",
        "headline": title,
        "name": title,
        "author": [({"@id": SITE + "#person"} if x == ME else {"@type": "Person", "name": x}) for x in au],
        "datePublished": str(yr),
        "isPartOf": {"@type": "Periodical" if t == "journal" else "CreativeWork", "name": html.unescape(venue)},
    }
    if doi:
        a["url"] = "https://doi.org/" + doi
        a["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": doi}
    elif pid in ARXIV:
        a["url"] = ARXIV[pid]
    if pdf:
        a["encoding"] = {"@type": "MediaObject", "encodingFormat": "application/pdf", "contentUrl": SITE + "assets/papers/" + pdf}
    if pid in ABS:
        a["abstract"] = ABS[pid]
    if award:
        a["award"] = html.unescape(award)
    return a

jsonld = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "Publications of Soyed Tuhin Ahmed",
    "url": SITE + "publications.html",
    "about": {"@type": "Person", "@id": SITE + "#person", "name": ME, "url": SITE},
    "hasPart": [article(p) for p in P],
}
jsonld_html = ('  <script type="application/ld+json">\n'
               + json.dumps(jsonld, indent=1, ensure_ascii=False).replace("</", "<\\/")
               + "\n  </script>")

def fill(tpl, replacements, out):
    t = open(os.path.join(HERE, tpl), encoding="utf-8").read()
    t = t.replace("<!DOCTYPE html>", "<!DOCTYPE html>\n<!-- GENERATED by _src/build.py from _src/" + tpl + ": edit the template, not this file -->", 1)
    for marker, content in replacements.items():
        t = t.replace(marker, content)
    open(os.path.join(ROOT, out), "w", encoding="utf-8").write(t)

fill("index.template.html", {"<!--SELECTED_PUBS-->": sel}, "index.html")
fill("publications.template.html", {"<!--FULL_PUBS-->": full, "<!--PUBS_JSONLD-->": jsonld_html}, "publications.html")
print(len(P), "pubs;", sum(p[1]=="journal" for p in P), "journal;", sum(p[1]=="conference" for p in P), "conference;",
      sum(p[5][0]==ME and p[1] in ("journal","conference") for p in P), "first-author peer-reviewed")
