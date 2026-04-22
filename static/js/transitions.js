// ═══════════════════════════════════════════════════════
//  PAGE TRANSITIONS
// ═══════════════════════════════════════════════════════

const overlay = document.getElementById('page-transition');

// On page load — slide overlay out
window.addEventListener('DOMContentLoaded', () => {
  if (overlay) {
    overlay.classList.add('is-entering');
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        overlay.classList.remove('is-entering');
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

  if (overlay) {
    overlay.classList.add('is-entering');
    setTimeout(() => {
      window.location.href = href;
    }, 480);
  } else {
    window.location.href = href;
  }
});

// ═══════════════════════════════════════════════════════
//  SCROLL-TRIGGERED ANIMATIONS
// ═══════════════════════════════════════════════════════

const animateEls = document.querySelectorAll('.animate-on-scroll');

if (animateEls.length > 0) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px',
    }
  );

  animateEls.forEach((el) => observer.observe(el));
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
  });
}

// ═══════════════════════════════════════════════════════
//  STICKY PLACE NAV (active state on scroll)
// ═══════════════════════════════════════════════════════

const placeNavItems = document.querySelectorAll('.place-nav-item');
if (placeNavItems.length > 0) {
  const sections = ['attractions', 'delicacies', 'festivals', 'myths']
    .map(id => document.getElementById(id))
    .filter(Boolean);

  const setActive = () => {
    let current = '';
    sections.forEach(section => {
      const rect = section.getBoundingClientRect();
      if (rect.top <= 200) {
        current = section.id;
      }
    });

    placeNavItems.forEach(item => {
      const href = item.getAttribute('href').replace('#', '');
      item.classList.toggle('active', href === current);
    });
  };

  window.addEventListener('scroll', setActive, { passive: true });
  setActive();
}

// ═══════════════════════════════════════════════════════
//  SMOOTH SCROLL for anchor links
// ═══════════════════════════════════════════════════════

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ═══════════════════════════════════════════════════════
//  WIP MODAL (kept from original for Sorsogon)
// ═══════════════════════════════════════════════════════

const wipOverlay = document.getElementById('wip-overlay');
const wipTitle = document.getElementById('wip-title');
const wipClose = document.getElementById('wip-close');

if (wipOverlay) {
  document.querySelectorAll('.wip-trigger').forEach(btn => {
    btn.addEventListener('click', () => {
      if (wipTitle) wipTitle.textContent = btn.dataset.name || '';
      wipOverlay.classList.add('active');
    });
  });

  if (wipClose) {
    wipClose.addEventListener('click', () => {
      wipOverlay.classList.remove('active');
    });
  }

  wipOverlay.addEventListener('click', (e) => {
    if (e.target === wipOverlay) wipOverlay.classList.remove('active');
  });
}

// ═══════════════════════════════════════════════════════
//  NAV TOGGLE (mobile)
// ═══════════════════════════════════════════════════════

const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    navToggle.classList.toggle('active');
  });
}

// ═══════════════════════════════════════════════════════
//  STAGGER animation-delay on items-grid children
// ═══════════════════════════════════════════════════════

document.querySelectorAll('.items-grid').forEach(grid => {
  grid.querySelectorAll('.animate-on-scroll').forEach((card, i) => {
    card.style.transitionDelay = `${i * 0.08}s`;
  });
});
