/* ═══════════════════════════════════════════════════════
   THIAGO BANDEIRA · PORTFOLIO · SCRIPT.JS v4
   Glass Tilt · Mesh Gradients · Premium Interactions
   ======================================================= */

/* ─── PRELOADER ─── */
window.addEventListener('load', () => {
    const pl = document.getElementById('preloader');
    if (pl) {
        setTimeout(() => pl.classList.add('hidden'), 1500);
    }
});

document.addEventListener('DOMContentLoaded', () => {

    /* ─────────────────────────────────────────────
       0. HERO SECTION (STATIC)
          Clean & Stable Professional Composition
    ───────────────────────────────────────────── */


    /* ─────────────────────────────────────────────
       0b. GLASS TILT ENGINE — Framer Motion parity
           Spring-physics rotation, gradient border
           angle, and specular shine follow
    ───────────────────────────────────────────── */
    const TILT_MAX    = 8;     // max degrees
    const TILT_SPRING = 0.15;  // Mais rígido (mais rápido)
    const TILT_DAMP   = 0.82;  // Menos "arrasto", mais direto

    document.querySelectorAll('.pcard').forEach(card => {
        let targetX = 0, targetY = 0;
        let currentX = 0, currentY = 0;
        let velX = 0, velY = 0;
        let rafId = null;
        let isHovered = false;
        let sX = 50, sY = 50;

        const shineEl = card.querySelector('.pcard-shine');

        function animate() {
            // Spring physics: velocity + damping
            velX = (velX + (targetX - currentX) * TILT_SPRING) * TILT_DAMP;
            velY = (velY + (targetY - currentY) * TILT_SPRING) * TILT_DAMP;
            currentX += velX;
            currentY += velY;

            // Batch style updates
            card.style.transform = `perspective(1000px) rotateX(${currentX.toFixed(2)}deg) rotateY(${currentY.toFixed(2)}deg) scale3d(1.02, 1.02, 1.02)`;
            
            // Specular shine update in the same frame
            if (shineEl) {
                shineEl.style.background = `radial-gradient(ellipse 55% 45% at ${sX}% ${sY}%, rgba(255,255,255,0.13) 0%, rgba(255,255,255,0.04) 40%, transparent 70%)`;
            }

            // Continue if still moving meaningfully
            if (isHovered || Math.abs(velX) > 0.01 || Math.abs(velY) > 0.01) {
                rafId = requestAnimationFrame(animate);
            } else {
                currentX = 0; currentY = 0;
                card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
                rafId = null;
            }
        }

        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const cx = (e.clientX - rect.left) / rect.width  - 0.5;
            const cy = (e.clientY - rect.top)  / rect.height - 0.5;

            targetY =  cx * TILT_MAX * 2;
            targetX = -cy * TILT_MAX * 2;

            sX = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1);
            sY = ((e.clientY - rect.top)  / rect.height * 100).toFixed(1);

            if (!rafId) rafId = requestAnimationFrame(animate);
        });

        card.addEventListener('mouseenter', () => {
            isHovered = true;
            card.style.transition = 'box-shadow 0.3s, filter 0.3s';
            if (!rafId) rafId = requestAnimationFrame(animate);
        });

        card.addEventListener('mouseleave', () => {
            isHovered = false;
            targetX = 0; targetY = 0;
            if (!rafId) rafId = requestAnimationFrame(animate);
        });
    });


    /* ─────────────────────────────────────────────
       0c. HERO CONTENT PARALLAX — light depth cue
           Hero text reacts subtly to mouse pos
    ───────────────────────────────────────────── */
    // Combined into main animateHero for performance efficiency



    /* ─────────────────────────────────────────────
    1. CUSTOM CURSOR (Disable on Mobile/Touch)
    ───────────────────────────────────────────── */
    const cursor = document.getElementById('cursor');
    const ring = document.querySelector('.cursor-ring');
    const dot = document.querySelector('.cursor-dot');

    if (window.innerWidth > 1024 && cursor) {
        let mouseX = -100, mouseY = -100;
        
        document.addEventListener('mousemove', e => {
            mouseX = e.clientX;
            mouseY = e.clientY;

            const posTransition = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
            if (dot) dot.style.transform = posTransition;
            if (ring) ring.style.transform = posTransition;

            const interactiveElements = document.querySelectorAll('.pcard:hover, .contact-glass-form:hover, .social-pill:hover, .btn-cv-premium:hover');
            interactiveElements.forEach(el => {
                const r = el.getBoundingClientRect();
                el.style.setProperty('--mx', `${((e.clientX - r.left) / r.width  * 100).toFixed(1)}%`);
                el.style.setProperty('--my', `${((e.clientY - r.top)  / r.height * 100).toFixed(1)}%`);
            });
        });

        document.querySelectorAll('a, button, .pcard, .gitem, .social-pill').forEach(el => {
            el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
            el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
        });
        document.addEventListener('mousedown', () => document.body.classList.add('cursor-click'));
        document.addEventListener('mouseup',   () => document.body.classList.remove('cursor-click'));
    }


    /* ─────────────────────────────────────────────
       3. REAL-TIME HUD (Simplified)
    ───────────────────────────────────────────── */
    // No specific JS needed for the simplified blinking red dot


    /* ─────────────────────────────────────────────
       4. SCROLL REVEAL
    ───────────────────────────────────────────── */
    const revealObs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add('visible');
                revealObs.unobserve(e.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-in').forEach(el => revealObs.observe(el));


    /* ─────────────────────────────────────────────
       5. NAVBAR — scrolled state
    ───────────────────────────────────────────── */
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (navbar) navbar.classList.toggle('scrolled', window.scrollY > 80);
    }, { passive: true });


    /* ─────────────────────────────────────────────
       6. VIDEO MODAL
    ───────────────────────────────────────────── */
    const videoModal = document.getElementById('videoModal');
    const videoIframe = document.getElementById('videoIframe');
    const closeBtn    = document.getElementById('closeModal');

    document.querySelectorAll('.pcard').forEach(card => {
        card.addEventListener('click', e => {
            e.preventDefault();
            const id = card.getAttribute('data-video-id');
            if (!id) return;
            videoIframe.src = `https://www.youtube.com/embed/${id}?autoplay=1&rel=0&modestbranding=1`;
            videoModal.classList.add('active');
            document.body.style.overflow = 'hidden';
            if (window.innerWidth <= 768) {
                // Focus on player
                videoModal.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    const closeVideo = () => {
        videoModal?.classList.remove('active');
        if (videoIframe) videoIframe.src = '';
        document.body.style.overflow = '';
    };
    closeBtn?.addEventListener('click', closeVideo);
    videoModal?.addEventListener('click', e => { if (e.target === videoModal) closeVideo(); });


    /* ─────────────────────────────────────────────
       7. PORTFOLIO FILTER LOGIC
    ───────────────────────────────────────────── */
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.pcard-wrap');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.getAttribute('data-filter');
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            projectCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filter === 'all' || category === filter) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 400);
                }
            });
        });
    });

    /* ─────────────────────────────────────────────
       8. IMAGE MODAL
    ───────────────────────────────────────────── */
    const imgModal     = document.getElementById('imageModal');
    const modalImg     = document.getElementById('modalImg');
    const closeImgBtn  = document.getElementById('closeImageModal');
    const imgPrev      = document.getElementById('imgPrev');
    const imgNext      = document.getElementById('imgNext');
    let currentImgIdx  = 0;
    const galleryItems = Array.from(document.querySelectorAll('.gitem:not([aria-hidden="true"])'));

    const updateModalImg = (idx) => {
        const item = galleryItems[idx];
        if (!item || !modalImg) return;
        const img = item.querySelector('img');
        if (!img) return;
        modalImg.style.opacity = '0';
        setTimeout(() => {
            modalImg.src = img.src;
            modalImg.alt = img.alt;
            modalImg.style.opacity = '1';
        }, 150);
        currentImgIdx = idx;
    };

    galleryItems.forEach((item, idx) => {
        item.addEventListener('click', () => {
            updateModalImg(idx);
            imgModal?.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    const closeImg = () => {
        imgModal?.classList.remove('active');
        document.body.style.overflow = '';
    };

    closeImgBtn?.addEventListener('click', closeImg);
    imgModal?.addEventListener('click', e => { if (e.target === imgModal) closeImg(); });
    imgPrev?.addEventListener('click', e => { e.stopPropagation(); updateModalImg((currentImgIdx - 1 + galleryItems.length) % galleryItems.length); });
    imgNext?.addEventListener('click', e => { e.stopPropagation(); updateModalImg((currentImgIdx + 1) % galleryItems.length); });

    document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeVideo(); closeImg(); } });

    /* ─────────────────────────────────────────────
       12. SKILLS BARS
    ───────────────────────────────────────────── */
    const skillsObs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.querySelectorAll('.skill-bar-fill').forEach(bar => {
                const pct = bar.getAttribute('data-pct');
                if (pct) bar.style.width = pct + '%';
            });
            skillsObs.unobserve(entry.target);
        });
    }, { threshold: 0.2 });

    const skillsBlock = document.getElementById('skills-block');
    if (skillsBlock) skillsObs.observe(skillsBlock);


    /* ─────────────────────────────────────────────
       13. STATS COUNTER
    ───────────────────────────────────────────── */
    const statsSection = document.querySelector('.section-stats');
    const statsObs = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting) {
            document.querySelectorAll('.stat-number').forEach(num => {
                const target = +num.getAttribute('data-target');
                const duration = 2000;
                const startTime = performance.now();
                function count(currentTime) {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    num.textContent = Math.floor(progress * target) + (target > 5 ? '+' : '');
                    if (progress < 1) requestAnimationFrame(count);
                    else num.textContent = target + (target > 5 ? '+' : '');
                }
                requestAnimationFrame(count);
            });
            statsObs.unobserve(statsSection);
        }
    }, { threshold: 0.5 });
    if (statsSection) statsObs.observe(statsSection);


    /* ─────────────────────────────────────────────
       10. WHATSAPP CONTACT FORM
    ───────────────────────────────────────────── */
    document.getElementById('whatsapp-form')?.addEventListener('submit', e => {
        e.preventDefault();
        const name    = document.getElementById('name')?.value.trim()    || '';
        const email   = document.getElementById('email')?.value.trim()   || '';
        const message = document.getElementById('message')?.value.trim() || '';
        const text    = `Olá Thiago! Meu nome é *${name}* (${email}).\n\n${message}`;
        window.open(`https://wa.me/5527997475747?text=${encodeURIComponent(text)}`, '_blank');
        const btn = e.target.querySelector('button[type="submit"]');
        if (btn) {
            const orig = btn.innerHTML;
            btn.innerHTML = '<span>ENVIADO ✓</span>';
            btn.style.background = 'rgba(22,163,74,0.4)';
            setTimeout(() => { btn.innerHTML = orig; btn.style.background = ''; }, 3000);
        }
    });

    /* ─────────────────────────────────────────────
       14. MOBILE BOTTOM NAV — Scroll Sync & Reveal
    ───────────────────────────────────────────── */
    const mobileNavItems = document.querySelectorAll('.mb-nav-item');
    const sections = document.querySelectorAll('section[id]');
    
    // Improved Sync with active state detection
    const syncMobileNav = () => {
        if (window.innerWidth > 1024) return;
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (window.scrollY >= sectionTop - (sectionHeight / 3)) {
                current = section.getAttribute('id');
            }
        });
        
        // Final fallback for bottom
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 50) {
            current = 'contato';
        }

        mobileNavItems.forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href') === `#${current}`) {
                item.classList.add('active');
            }
        });
    };

    // Scroll Reveal for Section Content (Mobile)
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-visible');
            }
        });
    }, { threshold: 0.15 });

    sections.forEach(section => {
        section.classList.add('mobile-reveal');
        sectionObserver.observe(section);
    });

    window.addEventListener('scroll', syncMobileNav, { passive: true });
    window.addEventListener('scroll', () => {
        // Subtle parallax for hero img on mobile scroll
        const heroImg = document.querySelector('.hero-main-img');
        if (window.innerWidth <= 768 && heroImg) {
            let scroll = window.scrollY;
            heroImg.style.transform = `scale(1.1) translateY(${scroll * 0.15}px)`;
        }
    }, { passive: true });
});
