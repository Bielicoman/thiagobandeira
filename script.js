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
    const TILT_SPRING = 0.10;  // lerp factor (stiffness)
    const TILT_DAMP   = 0.85;  // velocity damping

    document.querySelectorAll('.pcard').forEach(card => {
        let targetX = 0, targetY = 0;
        let currentX = 0, currentY = 0;
        let velX = 0, velY = 0;
        let rafId = null;
        let isHovered = false;

        const shineEl = card.querySelector('.pcard-shine');

        function animate() {
            // Spring physics: velocity + damping
            velX = (velX + (targetX - currentX) * TILT_SPRING) * TILT_DAMP;
            velY = (velY + (targetY - currentY) * TILT_SPRING) * TILT_DAMP;
            currentX += velX;
            currentY += velY;

            card.style.setProperty('--tilt-x', `${currentX.toFixed(3)}deg`);
            card.style.setProperty('--tilt-y', `${currentY.toFixed(3)}deg`);

            // Gradient border angle — rotates to face the light
            const angle = Math.atan2(currentX, -currentY) * (180 / Math.PI) + 135;
            card.style.setProperty('--tilt-border-angle', `${angle.toFixed(1)}deg`);

            // Continue if still moving meaningfully
            if (isHovered || Math.abs(velX) > 0.01 || Math.abs(velY) > 0.01) {
                rafId = requestAnimationFrame(animate);
            } else {
                // Snap to rest
                currentX = 0; currentY = 0;
                card.style.setProperty('--tilt-x', '0deg');
                card.style.setProperty('--tilt-y', '0deg');
                card.style.setProperty('--tilt-border-angle', '135deg');
                rafId = null;
            }
        }

        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const cx = (e.clientX - rect.left) / rect.width  - 0.5; // -0.5 to +0.5
            const cy = (e.clientY - rect.top)  / rect.height - 0.5;

            targetY =  cx * TILT_MAX * 2;
            targetX = -cy * TILT_MAX * 2;

            // Update specular shine position
            const shineX = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1);
            const shineY = ((e.clientY - rect.top)  / rect.height * 100).toFixed(1);
            card.style.setProperty('--tilt-shine-x', `${shineX}%`);
            card.style.setProperty('--tilt-shine-y', `${shineY}%`);
            if (shineEl) {
                shineEl.style.background = `radial-gradient(ellipse 55% 45% at ${shineX}% ${shineY}%, rgba(255,255,255,0.13) 0%, rgba(255,255,255,0.04) 40%, transparent 70%)`;
            }

            if (!rafId) rafId = requestAnimationFrame(animate);
        });

        card.addEventListener('mouseenter', () => {
            isHovered = true;
            card.style.transition = 'box-shadow 0.5s, filter 0.4s';
            if (!rafId) rafId = requestAnimationFrame(animate);
        });

        card.addEventListener('mouseleave', () => {
            isHovered = false;
            targetX = 0; targetY = 0;
            // Spring will naturally return to 0
            if (!rafId) rafId = requestAnimationFrame(animate);
        });
    });


    /* ─────────────────────────────────────────────
       0c. HERO CONTENT PARALLAX — light depth cue
           Hero text reacts subtly to mouse pos
    ───────────────────────────────────────────── */
    // Combined into main animateHero for performance efficiency



    /* ─────────────────────────────────────────────
    1. CUSTOM CURSOR (HUD Mira 1:1 + Ring Lerp)
    ───────────────────────────────────────────── */
    const cursor = document.getElementById('cursor');
    const ring = document.querySelector('.cursor-ring');
    const dot = document.querySelector('.cursor-dot');

    let mouseX = -100, mouseY = -100;
    let ringX  = -100, ringY  = -100;

    document.addEventListener('mousemove', e => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        // Mira (Dot) follows 1:1 instantly
        if (dot) {
            dot.style.left = `${mouseX}px`;
            dot.style.top  = `${mouseY}px`;
        }

        // Liquid glass specular tracking on interactive elements
        document.querySelectorAll('.pcard, .contact-glass-form, .social-pill, .btn-cv-premium').forEach(el => {
            const r = el.getBoundingClientRect();
            el.style.setProperty('--mx', `${((e.clientX - r.left) / r.width  * 100).toFixed(1)}%`);
            el.style.setProperty('--my', `${((e.clientY - r.top)  / r.height * 100).toFixed(1)}%`);
        });
    });

    (function lerpRing() {
        ringX += (mouseX - ringX) * 0.15;
        ringY += (mouseY - ringY) * 0.15;
        if (ring) {
            ring.style.left = `${ringX}px`;
            ring.style.top  = `${ringY}px`;
        }
        requestAnimationFrame(lerpRing);
    })();

    document.querySelectorAll('a, button, .pcard, .gitem, .social-pill').forEach(el => {
        el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
        el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
    });
    document.addEventListener('mousedown', () => document.body.classList.add('cursor-click'));
    document.addEventListener('mouseup',   () => document.body.classList.remove('cursor-click'));


    // HERO SLIDESHOW REMOVED IN FAVOR OF CINEMATIC DEPTH LAYOUT


    /* ─────────────────────────────────────────────
       3. REAL-TIME TIMECODE (viewfinder HUD)
    ───────────────────────────────────────────── */
    const timecodeEl = document.getElementById('realTimecode');
    if (timecodeEl) {
        const p = n => String(n).padStart(2, '0');
        setInterval(() => {
            const now = new Date();
            const f = p(Math.floor((now.getMilliseconds() / 1000) * 24));
            timecodeEl.textContent =
                ` REC ${p(now.getHours())}:${p(now.getMinutes())}:${p(now.getSeconds())}:${f}`;
        }, 40);
    }


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
        navbar.classList.toggle('scrolled', window.scrollY > 80);
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
        });
    });

    const closeVideo = () => {
        videoModal.classList.remove('active');
        videoIframe.src = '';
        document.body.style.overflow = '';
    };
    closeBtn?.addEventListener('click', closeVideo);
    videoModal?.addEventListener('click', e => { if (e.target === videoModal) closeVideo(); });


    /* ─────────────────────────────────────────────
       7. GALLERY — auto-scroll (CSS-driven)
          Click opens image modal
    ───────────────────────────────────────────── */

    /* ─────────────────────────────────────────────
       8. GALLERY IMAGE MODAL
    ───────────────────────────────────────────── */
    const imgModal    = document.getElementById('imageModal');
    const modalImg    = document.getElementById('modalImg');
    const closeImgBtn = document.getElementById('closeImageModal');
    // Bind clicks on ALL .gitem elements
    document.querySelectorAll('.gitem').forEach(item => {
        item.addEventListener('click', () => {
            if (item.getAttribute('aria-hidden') === 'true') return; // skip duplicates
            const img = item.querySelector('img');
            if (!img || !imgModal) return;
            modalImg.src = img.src;
            modalImg.alt = img.alt;
            imgModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    const closeImg = () => {
        imgModal?.classList.remove('active');
        if (modalImg) modalImg.src = '';
        document.body.style.overflow = '';
    };
    closeImgBtn?.addEventListener('click', closeImg);
    imgModal?.addEventListener('click', e => { if (e.target === imgModal) closeImg(); });


    /* ─────────────────────────────────────────────
       9. ESC key closes any modal
    ───────────────────────────────────────────── */
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape') { closeVideo(); closeImg(); }
    });


    /* ─────────────────────────────────────────────
       11. THEME TOGGLE (dark / light)
    ───────────────────────────────────────────── */
    const themeToggle = document.getElementById('theme-toggle');
    const savedTheme  = localStorage.getItem('tb-theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);

    themeToggle?.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next    = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('tb-theme', next);
    });


    /* ─────────────────────────────────────────────
       12. SKILLS BARS — animate on scroll entry
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
       13. STATS COUNTER — intersection based
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
                    const currentCount = Math.floor(progress * target);
                    num.textContent = currentCount + (target > 5 ? '+' : '');
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

});
