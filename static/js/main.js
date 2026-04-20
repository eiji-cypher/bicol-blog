// Bicol Blog — Main JS

// WIP modal
const wipOverlay = document.getElementById('wip-overlay');
const wipTitle = document.getElementById('wip-title');
const wipClose = document.getElementById('wip-close');
document.querySelectorAll('.wip-trigger').forEach(btn => {
    btn.addEventListener('click', () => {
        wipTitle.textContent = btn.dataset.name;
        wipOverlay.classList.add('active');
    });
});
if (wipClose) wipClose.addEventListener('click', () => wipOverlay.classList.remove('active'));
if (wipOverlay) wipOverlay.addEventListener('click', (e) => {
    if (e.target === wipOverlay) wipOverlay.classList.remove('active');
});

const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');
if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('open');
    });
    // Close on link click
    navLinks.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => navLinks.classList.remove('open'));
    });
}

// Smooth nav highlight on scroll
const sections = document.querySelectorAll('[id]');
const navLinks = document.querySelectorAll('.place-nav-item');

if (navLinks.length > 0) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.style.color = link.getAttribute('href') === `#${id}`
                        ? 'rgba(255,255,255,0.95)'
                        : 'rgba(255,255,255,0.5)';
                });
            }
        });
    }, { threshold: 0.3 });

    sections.forEach(section => observer.observe(section));
}

// Animate items on scroll into view
const animatedItems = document.querySelectorAll('.item-card, .festival-item, .myth-item, .place-card');

const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }, i * 60);
            fadeInObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

animatedItems.forEach(item => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(20px)';
    item.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    fadeInObserver.observe(item);
});

// Header scroll shadow
const header = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
        header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
    } else {
        header.style.boxShadow = 'none';
    }
});
