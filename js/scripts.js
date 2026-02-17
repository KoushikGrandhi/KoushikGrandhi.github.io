/*!
    * Start Bootstrap - Resume v6.0.2 (https://startbootstrap.com/theme/resume)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE)
    */
(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
                this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top,
                    },
                    5,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#sideNav",
    });
})(jQuery); // End of use strict

(function () {
    "use strict";

    var root = document.documentElement;
    var toTopButton = document.getElementById("toTop");
    var progressBar = document.querySelector(".scroll-progress");
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var canTilt = !reduceMotion && window.matchMedia("(pointer: fine)").matches;

    var revealTargets = Array.from(
        document.querySelectorAll(
            ".resume-section .resume-section-content, .resume-section .d-flex.flex-column.flex-md-row.justify-content-between, .social-icons .social-icon"
        )
    );

    revealTargets.forEach(function (element, index) {
        element.classList.add("reveal-on-scroll");
        element.style.setProperty("--reveal-delay", Math.min(index * 45, 260) + "ms");
    });

    if ("IntersectionObserver" in window) {
        var revealObserver = new IntersectionObserver(
            function (entries, observer) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.2, rootMargin: "0px 0px -10% 0px" }
        );
        revealTargets.forEach(function (element) {
            revealObserver.observe(element);
        });
    } else {
        revealTargets.forEach(function (element) {
            element.classList.add("is-visible");
        });
    }

    var isTicking = false;
    function updateScrollState() {
        var maxScroll = document.documentElement.scrollHeight - window.innerHeight;
        var progress = maxScroll > 0 ? (window.scrollY / maxScroll) * 100 : 0;
        root.style.setProperty("--scroll-progress", progress.toFixed(2) + "%");
        if (progressBar) {
            progressBar.style.width = progress.toFixed(2) + "%";
        }
        if (toTopButton) {
            toTopButton.classList.toggle("is-visible", window.scrollY > 520);
        }
        isTicking = false;
    }

    function requestScrollSync() {
        if (!isTicking) {
            isTicking = true;
            window.requestAnimationFrame(updateScrollState);
        }
    }

    window.addEventListener("scroll", requestScrollSync, { passive: true });
    window.addEventListener("resize", requestScrollSync);
    updateScrollState();

    if (toTopButton) {
        toTopButton.addEventListener("click", function () {
            window.scrollTo({
                top: 0,
                behavior: reduceMotion ? "auto" : "smooth",
            });
        });
    }

    if (canTilt) {
        var cards = Array.from(
            document.querySelectorAll(".resume-section .d-flex.flex-column.flex-md-row.justify-content-between")
        );

        cards.forEach(function (card) {
            function resetCardTilt() {
                card.style.setProperty("--tilt-x", "0deg");
                card.style.setProperty("--tilt-y", "0deg");
                card.style.setProperty("--shine-x", "50%");
            }

            card.addEventListener("mousemove", function (event) {
                var bounds = card.getBoundingClientRect();
                var offsetX = event.clientX - bounds.left;
                var offsetY = event.clientY - bounds.top;
                var ratioX = offsetX / bounds.width - 0.5;
                var ratioY = offsetY / bounds.height - 0.5;
                var tiltX = (-ratioY * 4).toFixed(2);
                var tiltY = (ratioX * 5).toFixed(2);
                var shineX = ((ratioX + 0.5) * 100).toFixed(2);
                card.style.setProperty("--tilt-x", tiltX + "deg");
                card.style.setProperty("--tilt-y", tiltY + "deg");
                card.style.setProperty("--shine-x", shineX + "%");
            });

            card.addEventListener("mouseleave", resetCardTilt);
            card.addEventListener("blur", resetCardTilt, true);
        });
    }
})();
