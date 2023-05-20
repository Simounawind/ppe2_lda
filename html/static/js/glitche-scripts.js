$(function () {
  $(window).unload(function () {});
  var g = $(window).width();
  var d = $(window).height();
  $(".section.started").css({ height: d - 60 });
  $(".typed-load").typed({ stringsElement: $(".typing-load"), loop: true });
  $(window).load(function () {
    $(".preloader .pre-inner").fadeOut(800, function () {
      $(".preloader").fadeOut();
      $("body").addClass("loaded");
      $(".typed-subtitle").typed({
        stringsElement: $(".typing-subtitle"),
        loop: true,
      });
      $(".typed-bread").typed({
        stringsElement: $(".typing-bread"),
        showCursor: false,
      });
      var i = location.hash;
      var h = $(i);
      if (i.indexOf("#section-") == 0 && h.length) {
        $("body, html").animate({ scrollTop: $(i).offset().top - 70 }, 400);
      }
    });
  });
  $("header .top-menu, .typed-bread").on("click", "a", function () {
    var h = $(this).attr("href");
    if (h.indexOf("#section-") == 0) {
      if (!$("body").hasClass("home")) {
        location.href = "/" + h;
      }
      $("body, html").animate({ scrollTop: $(h).offset().top - 110 }, 400);
      if ($("header").hasClass("active")) {
        $(".menu-btn").trigger("click");
      }
    } else {
      $("body").removeClass("loaded");
      setTimeout(function () {
        location.href = "" + h;
      }, 500);
    }
    return false;
  });
  $("header").on("click", ".menu-btn", function () {
    if ($("header").hasClass("active")) {
      $("header").removeClass("active");
      $("body").addClass("loaded");
    } else {
      $("header").addClass("active");
      $("body").removeClass("loaded");
    }
    return false;
  });
  $(window).scroll(function () {
    if ($(this).scrollTop() >= 1) {
      $(".mouse_btn").fadeOut();
    } else {
      $(".mouse_btn").fadeIn();
    }
  });
  $(".section").on("click", ".mouse_btn", function () {
    $("body,html").animate({ scrollTop: d - 150 }, 800);
  });
  $("body").on(
    {
      mouseenter: function () {
        $(this).addClass("glitch-effect-white");
      },
      mouseleave: function () {
        $(this).removeClass("glitch-effect-white");
        $(".top-menu ul li.active a.btn").addClass("glitch-effect-white");
      },
    },
    "a.btn, .btn"
  );
  $("#cform").validate({
    rules: {
      name: { required: true },
      message: { required: true },
      email: { required: true, email: true },
    },
    success: "valid",
    submitHandler: function () {
      $.ajax({
        url: "mailer/feedback.php",
        type: "post",
        dataType: "json",
        data:
          "name=" +
          $("#cform").find('input[name="name"]').val() +
          "&email=" +
          $("#cform").find('input[name="email"]').val() +
          "&message=" +
          $("#cform").find('textarea[name="message"]').val(),
        beforeSend: function () {},
        complete: function () {},
        success: function (h) {
          $("#cform").fadeOut();
          $(".alert-success").delay(1000).fadeIn();
        },
      });
    },
  });
  $("#comment_form").validate({
    rules: {
      name: { required: true },
      message: { required: true },
      email: { required: true, email: true },
    },
    success: "valid",
    submitHandler: function () {},
  });
  var c = $(".section.clients .box-items");
  c.imagesLoaded(function () {
    c.isotope({ itemSelector: ".box-item" });
  });
  var b = $(".section.blog .box-items");
  b.imagesLoaded(function () {
    b.isotope({ itemSelector: ".box-item" });
  });
  var a = $(".section.works .box-items");
  a.imagesLoaded(function () {
    a.isotope({ itemSelector: ".box-item" });
  });
  $(".filters").on("click", ".btn-group", function () {
    var h = $(this).find("input").val();
    a.isotope({ filter: h });
    $(".filters .btn-group label").removeClass("glitch-effect");
    $(this).find("label").addClass("glitch-effect");
  });
  if (
    /\.(?:jpg|jpeg|gif|png)$/i.test($(".gallery-item:first a").attr("href"))
  ) {
    $(".gallery-item a").magnificPopup({
      gallery: { enabled: true },
      type: "image",
      closeBtnInside: false,
      mainClass: "mfp-fade",
    });
  }
  $(".has-popup-media").magnificPopup({
    type: "inline",
    overflowY: "auto",
    closeBtnInside: true,
    mainClass: "mfp-fade",
  });
  $(".has-popup-image").magnificPopup({
    type: "image",
    closeOnContentClick: true,
    mainClass: "mfp-fade",
    image: { verticalFit: true },
  });
  $(".has-popup-video").magnificPopup({
    disableOn: 700,
    type: "iframe",
    iframe: {
      patterns: {
        youtube_short: {
          index: "youtu.be/",
          id: "youtu.be/",
          src: "https://www.youtube.com/embed/%id%?autoplay=1",
        },
      },
    },
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false,
    mainClass: "mfp-fade",
    callbacks: {
      markupParse: function (i, j, h) {
        i.find("iframe").attr("allow", "autoplay");
      },
    },
  });
  $(".has-popup-music").magnificPopup({
    disableOn: 700,
    type: "iframe",
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false,
    mainClass: "mfp-fade",
  });
  $(".has-popup-gallery").on("click", function () {
    var h = $(this).attr("href");
    $(h)
      .magnificPopup({
        delegate: "a",
        type: "image",
        closeOnContentClick: false,
        mainClass: "mfp-fade",
        removalDelay: 160,
        fixedContentPos: false,
        gallery: { enabled: true },
      })
      .magnificPopup("open");
    return false;
  });
  $(window).resize(function () {
    var k = $(window).width();
    var h = $(window).height();
    $(".section.started").css({ height: h - 60 });
    var i = $(".skills-list.dotted .progress");
    var j = i.width();
    if (i.length) {
      i.find(".percentage .da").css({ width: j + 1 });
    }
  });
  if (g < 840) {
    $(".section.started").css({ height: d - 30 });
  }
  if ($(".section").length && $(".top-menu li a").length) {
    $(window).on("scroll", function () {
      var h = $(window).scrollTop();
      $(".top-menu ul li a").each(function () {
        if ($(this).attr("href").indexOf("#section-") == 0) {
          var i = $(this);
          var j = $(i.attr("href"));
          if (j.length) {
            if (j.offset().top <= h + 120) {
              $(".top-menu ul li").removeClass("active");
              i.closest("li").addClass("active");
            }
          }
          if (h == 0) {
            $(".top-menu ul li").removeClass("active");
          }
        }
      });
    });
  }
  function e() {
    var h = $(".skills.dotted .progress");
    var i = h.width();
    if (h.length) {
      h.append(
        '<span class="dg"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span>'
      );
      h.find(".percentage").append(
        '<span class="da"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span>'
      );
      h.find(".percentage .da").css({ width: i });
    }
  }
  setTimeout(e, 1000);
  var f = $(".skills.circles .progress");
  if (f.length) {
    f.append(
      '<div class="slice"><div class="bar"></div><div class="fill"></div></div>'
    );
  }
});
