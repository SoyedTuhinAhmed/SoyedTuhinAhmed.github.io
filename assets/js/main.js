// Theme toggle (remembers choice; defaults to OS preference)
(function () {
  const root = document.documentElement;
  const saved = localStorage.getItem('theme');
  if (saved) root.setAttribute('data-theme', saved);
  else if (window.matchMedia('(prefers-color-scheme: dark)').matches) root.setAttribute('data-theme', 'dark');

  document.addEventListener('DOMContentLoaded', () => {
    const themeBtn = document.getElementById('theme-toggle');
    const setIcon = () => {
      if (!themeBtn) return;
      const dark = root.getAttribute('data-theme') === 'dark';
      themeBtn.innerHTML = dark ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
    };
    setIcon();
    themeBtn && themeBtn.addEventListener('click', () => {
      const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      setIcon();
    });

    // Mobile menu
    const menuBtn = document.getElementById('menu-toggle');
    const links = document.getElementById('nav-links');
    menuBtn && menuBtn.addEventListener('click', () => links.classList.toggle('open'));
    links && links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));

    // Abstract toggles
    document.querySelectorAll('[data-abs]').forEach(btn => {
      btn.addEventListener('click', () => {
        const el = document.getElementById(btn.dataset.abs);
        el.classList.toggle('open');
        btn.textContent = el.classList.contains('open') ? 'Hide abstract' : 'Abstract';
      });
    });

    // News expand
    const newsBtn = document.getElementById('news-more');
    newsBtn && newsBtn.addEventListener('click', () => {
      const list = document.getElementById('news-list');
      list.classList.toggle('expanded');
      newsBtn.textContent = list.classList.contains('expanded') ? 'Show less' : 'Show all news';
    });

    // Publication filters
    const filterBtns = document.querySelectorAll('.pub-filters button');
    filterBtns.forEach(b => b.addEventListener('click', () => {
      filterBtns.forEach(x => x.classList.remove('active'));
      b.classList.add('active');
      const f = b.dataset.filter;
      document.querySelectorAll('.pub[data-type]').forEach(p => {
        const show = f === 'all' || p.dataset.type === f || (f === 'first' && p.dataset.first === '1');
        p.classList.toggle('hidden', !show);
      });
      document.querySelectorAll('.year-group').forEach(g => {
        g.classList.toggle('hidden', !g.querySelector('.pub:not(.hidden)'));
      });
    }));

    // Active nav link on scroll
    const sections = [...document.querySelectorAll('section[id]')];
    const navAs = [...document.querySelectorAll('.nav-links a[href^="#"]')];
    if (sections.length && navAs.length && 'IntersectionObserver' in window) {
      const obs = new IntersectionObserver(entries => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            navAs.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
          }
        });
      }, { rootMargin: '-45% 0px -50% 0px' });
      sections.forEach(s => obs.observe(s));
    }

    // Reveal on scroll
    const rev = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
      const ro = new IntersectionObserver(entries => {
        entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); ro.unobserve(e.target); } });
      }, { threshold: 0.08 });
      rev.forEach(r => ro.observe(r));
    } else rev.forEach(r => r.classList.add('visible'));

    const y = document.getElementById('year');
    if (y) y.textContent = new Date().getFullYear();
  });
})();
