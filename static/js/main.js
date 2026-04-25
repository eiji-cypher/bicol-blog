// Bicol Blog — Main JS

// ═══════════════════════════════════════════════════════
//  SCROLL PROGRESS BAR
// ═══════════════════════════════════════════════════════
const progressBar = document.createElement('div');
progressBar.className = 'scroll-progress-bar';
document.body.appendChild(progressBar);

window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    progressBar.style.width = scrolled + '%';
}, { passive: true });

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
//  UPDATES MODAL
// ═══════════════════════════════════════════════════════
const updatesModal = document.getElementById('updates-modal');
const updatesModalCloseBtn = updatesModal ? updatesModal.querySelector('.updates-modal-close') : null;
const updatesModalAcknowledgeBtn = updatesModal ? updatesModal.querySelector('.updates-modal-acknowledge') : null;

if (updatesModal && !localStorage.getItem('updatesSeen')) {
    // Show modal after a short delay to ensure page is loaded
    setTimeout(() => {
        updatesModal.classList.add('is-visible');
    }, 1000); // Adjust delay as needed
}

const hideUpdatesModal = () => {
    if (updatesModal) {
        updatesModal.classList.remove('is-visible');
        localStorage.setItem('updatesSeen', 'true'); // Mark updates as seen
    }
};

if (updatesModalCloseBtn) { updatesModalCloseBtn.addEventListener('click', hideUpdatesModal); }
if (updatesModalAcknowledgeBtn) { updatesModalAcknowledgeBtn.addEventListener('click', hideUpdatesModal); }

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

// ═══════════════════════════════════════════════════════
//  MAGNETIC BUTTON EFFECT
// ═══════════════════════════════════════════════════════
const magneticButtons = document.querySelectorAll('.hero-cta');

magneticButtons.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
        const rect = btn.getBoundingClientRect();
        const x = (e.clientX - rect.left - rect.width / 2) * 0.4;
        const y = (e.clientY - rect.top - rect.height / 2) * 0.4;
        
        btn.classList.add('magnet-active');
        btn.style.transform = `translate(${x}px, ${y}px)`;
    });

    btn.addEventListener('mouseleave', () => {
        btn.classList.remove('magnet-active');
        btn.style.transform = '';
    });
});

// ═══════════════════════════════════════════════════════
//  HERO SPOTLIGHT EFFECT
// ═══════════════════════════════════════════════════════
const heroSection = document.querySelector('.hero');
if (heroSection) {
    heroSection.addEventListener('mousemove', (e) => {
        const rect = heroSection.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        heroSection.style.setProperty('--mouse-x', `${x}px`);
        heroSection.style.setProperty('--mouse-y', `${y}px`);
    });
}

// ═══════════════════════════════════════════════════════
//  3D TILT EFFECT FOR PLACE CARDS
// ═══════════════════════════════════════════════════════
const placeCards = document.querySelectorAll('.place-card');

placeCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = ((y - centerY) / centerY) * -8;
        const rotateY = ((x - centerX) / centerX) * 8;
        
        card.classList.add('tilt-active');
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px) scale(1.01)`;
    });

    card.addEventListener('mouseleave', () => {
        card.classList.remove('tilt-active');
        card.style.transform = '';
    });
});

// ═══════════════════════════════════════════════════════
//  CARD IMAGE PARALLAX EFFECT
// ═══════════════════════════════════════════════════════
const cardImages = document.querySelectorAll('.card-img');
if (cardImages.length > 0) {
    let tickingParallax = false;
    window.addEventListener('scroll', () => {
        if (!tickingParallax) {
            requestAnimationFrame(() => {
                const winHeight = window.innerHeight;
                cardImages.forEach(img => {
                    const rect = img.getBoundingClientRect();
                    if (rect.top < winHeight && rect.bottom > 0) {
                        const yPos = (rect.top / winHeight - 0.5) * -40;
                        img.style.setProperty('--parallax-y', `${yPos}px`);
                    }
                });
                tickingParallax = false;
            });
            tickingParallax = true;
        }
    }, { passive: true });
}
