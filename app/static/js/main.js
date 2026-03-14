document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Initialize Tilt Effect (on desktop)
    VanillaTilt.init(document.querySelectorAll(".glass-card"), {
        max: 10,
        speed: 400,
        glare: true,
        "max-glare": 0.3,
    });

    // 2. Scroll-Reveal Logic
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target); // Reveal only once
            }
        });
    }, observerOptions);

    // Initial State for Scroll Animation
    document.querySelectorAll('.glass-card').forEach(card => {
        card.style.opacity = "0";
        card.style.transform = "translateY(50px)";
        card.style.transition = "all 0.8s cubic-bezier(0.23, 1, 0.32, 1)";
        observer.observe(card);
    });

    // 3. Dynamic Cursor Glow (The "Luxury" Detail)
    const glow = document.querySelector('.bg-glow');
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth) * 100;
        const y = (e.clientY / window.innerHeight) * 100;
        glow.style.background = `radial-gradient(circle at ${x}% ${y}%, #1a1a1a, #050505)`;
    });
});
