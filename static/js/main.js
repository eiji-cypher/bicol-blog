// Bicol Blog — Main JS

// ═══════════════════════════════════════════════════════
//  SITE LOADER
// ═══════════════════════════════════════════════════════
window.addEventListener('load', () => {
    const loader = document.getElementById('site-loader');
    if (loader) {
        loader.classList.add('is-hidden');
        setTimeout(() => {
            loader.style.display = 'none';
        }, 600); // Wait for CSS opacity transition
    }
});

// ═══════════════════════════════════════════════════════
//  HAMBURGER MENU TOGGLE
// ═══════════════════════════════════════════════════════
const navToggle = document.getElementById('nav-toggle');
const navLinksEl = document.getElementById('nav-links');
if (navToggle && navLinksEl) {
    navToggle.addEventListener('click', () => {
        navLinksEl.classList.toggle('open');
        navToggle.classList.toggle('active'); // Add active class for styling the toggle button
    });
    navLinksEl.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => navLinksEl.classList.remove('open'));
    });
}

// ═══════════════════════════════════════════════════════
//  PAGE TRANSITIONS
// ═══════════════════════════════════════════════════════
const pageTransitionOverlay = document.getElementById('page-transition'); // Assuming a div with id="page-transition" exists in base.html for this

// On page load — slide overlay out
window.addEventListener('DOMContentLoaded', () => {
    if (pageTransitionOverlay) {
        pageTransitionOverlay.classList.add('is-entering');
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                pageTransitionOverlay.classList.remove('is-entering');
            });
        });
    }
});

// On link click — slide overlay in, then navigate
document.addEventListener('click', (e) => {
    const link = e.target.closest('a.js-page-link, a[href^="/"]');
    if (!link) return;

    const href = link.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('//')) return;
    if (e.ctrlKey || e.metaKey || e.shiftKey || link.target === '_blank') return;

    e.preventDefault();

    if (pageTransitionOverlay) {
        pageTransitionOverlay.classList.add('is-entering');
        setTimeout(() => {
            window.location.href = href;
        }, 480); // Match CSS transition duration
    } else {
        window.location.href = href;
    }
});

// ═══════════════════════════════════════════════════════
//  SCROLL-TRIGGERED ANIMATIONS (using .animate-on-scroll class)
// ═══════════════════════════════════════════════════════
const animateEls = document.querySelectorAll('.animate-on-scroll');

if (animateEls.length > 0) {
    const observer = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target); // Stop observing once visible
                }
            });
        },
        {
            threshold: 0.12, // Trigger when 12% of the item is visible
            rootMargin: '0px 0px -40px 0px', // Adjust detection area
        }
    );

    animateEls.forEach((el, i) => {
        // Apply staggered delay using a CSS custom property
        el.style.setProperty('--animation-delay', `${i * 0.08}s`);
        observer.observe(el);
    });
}

// ═══════════════════════════════════════════════════════
//  PARALLAX (detail hero background)
// ═══════════════════════════════════════════════════════
const detailHeroBg = document.querySelector('.detail-hero-bg');
if (detailHeroBg) {
    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(() => {
                const scrolled = window.pageYOffset;
                detailHeroBg.style.transform = `translateY(${scrolled * 0.35}px)`;
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });
}

// ═══════════════════════════════════════════════════════
//  SMOOTH SCROLL for anchor links
// ═══════════════════════════════════════════════════════
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
        const target = document.querySelector(anchor.getAttribute('href'));
        if (entry.isIntersecting) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ═══════════════════════════════════════════════════════
//  STICKY PLACE NAV (active state on scroll)
// ═══════════════════════════════════════════════════════
const placeNavItems = document.querySelectorAll('.place-nav-item');
if (placeNavItems.length > 0) {
    const sections = ['attractions', 'delicacies', 'festivals', 'myths']
        .map(id => document.getElementById(id))
        .filter(Boolean); // Filter out nulls if a section doesn't exist

    const setActive = () => {
        let current = '';
        // Find the section currently in view (or closest to the top)
        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            // Consider a section active if its top is within 200px from the viewport top
            if (rect.top <= 200 && rect.bottom > 0) {
                current = section.id;
            }
        });

        // Set active class on corresponding nav item
        placeNavItems.forEach(item => {
            const href = item.getAttribute('href').replace('#', '');
            item.classList.toggle('active', href === current);
        });
    };

    window.addEventListener('scroll', setActive, { passive: true });
    setActive(); // Set initial active state on load
}

// ═══════════════════════════════════════════════════════
//  HEADER SHADOW ON SCROLL
// ═══════════════════════════════════════════════════════
const header = document.querySelector('.site-header');
if (header) {
    window.addEventListener('scroll', () => {
        header.style.boxShadow = window.scrollY > 20
            ? '0 2px 24px rgba(0,0,0,0.1)'
            : 'none';
    }, { passive: true });
}
