// Bicol Blog — Main JS

// Hamburger menu toggle
const navToggle = document.getElementById('nav-toggle');
const navLinksEl = document.getElementById('nav-links');
if (navToggle && navLinksEl) {
    navToggle.addEventListener('click', () => {
        navLinksEl.classList.toggle('open');
    });
    navLinksEl.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => navLinksEl.classList.remove('open'));
    });
}

// WIP modal
const wipOverlay = document.getElementById('wip-overlay');
const wipTitle = document.getElementById('wip-title');
const wipClose = document.getElementById('wip-close');
document.querySelectorAll('.wip-trigger').forEach(btn => {
    btn.addEventListener('click', () => {
        if (wipTitle) wipTitle.textContent = btn.dataset.name;
        if (wipOverlay) wipOverlay.classList.add('active');
    });
});
if (wipClose) wipClose.addEventListener('click', () => wipOverlay.classList.remove('active'));
if (wipOverlay) wipOverlay.addEventListener('click', (e) => {
    if (e.target === wipOverlay) wipOverlay.classList.remove('active');
});

// Scroll-in animation for cards and sections
const scrollItems = document.querySelectorAll('.item-card, .festival-item, .myth-item, .place-card, .section-header, .other-card');
const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, i * 60);
            scrollObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.08 });

scrollItems.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity 0.55s ease, transform 0.55s ease';
    scrollObserver.observe(el);
});

// Active nav highlight on scroll (place pages)
const placeNavItems = document.querySelectorAll('.place-nav-item');
if (placeNavItems.length > 0) {
    const sectionIds = ['attractions', 'delicacies', 'festivals', 'myths'];
    const sectionEls = sectionIds.map(id => document.getElementById(id)).filter(Boolean);

    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                placeNavItems.forEach(link => {
                    const isActive = link.getAttribute('href') === `#${id}`;
                    link.style.color = isActive ? 'white' : 'rgba(255,255,255,0.5)';
                    link.style.background = isActive ? 'rgba(255,255,255,0.12)' : '';
                });
            }
        });
    }, { threshold: 0.35 });

    sectionEls.forEach(el => navObserver.observe(el));
}

// Header shadow on scroll
const header = document.querySelector('.site-header');
if (header) {
    window.addEventListener('scroll', () => {
        header.style.boxShadow = window.scrollY > 20
            ? '0 2px 24px rgba(0,0,0,0.1)'
            : 'none';
    }, { passive: true });
}
