import os
import json

# JSON to HTML blog generator
def generate_blogs_from_json(json_file):
    with open(json_file, 'r') as file:
        blogs = json.load(file)

    # Loop through each blog in the JSON file
    for blog in blogs:
        file_name = blog['file_name']
        title = blog['title']
        description = blog['description']
        image_path = blog['image_path']
        author = blog['author']
        date = blog['date']
        content = blog['content']
        keywords = blog['keywords']

        # Output file path
        output_file = f"{file_name}.html"

        # Skip if file already exists
        # if os.path.exists(output_file):
        #     print(f"File {output_file} already exists. Skipping...")
        #     continue

        # HTML structure
        html_content = f"""<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>BITS India - Business & IT Solutions - Innovating Defence & Commercial Technology</title>
  <meta content="" name="BITS India - Business & IT Solutions | Innovating Defence & Commercial Technology">
  <meta name="description" content="BITS India - Business & IT Solutions | Innovating Defence & Commercial Technology">

  <meta name="keywords" content={keywords}/>

  <!-- Favicons -->
  <link href="../assets/images/favicon.png" rel="icon">
  <link href="../assets/images/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="../../../css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600;1,700&amp;family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;display=swap" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
  <link href="../../../css2-1?family=Oswald:wght@500&amp;display=swap" rel="stylesheet">
  <link href="../../../css2-2?family=Poppins:wght@300;400&amp;display=swap" rel="stylesheet">
  <!-- Vendor CSS Files -->
  <link href="../assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="../assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="../assets/stylesheets/font-awesome.min.css" rel="stylesheet">
  <link href="../assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <!-- Main CSS File -->
  <link href="../assets/stylesheets/styles.css" rel="stylesheet">

</head>

<body>

  <header id="header" class="header d-flex align-items-center sticked stikcy-menu">
    <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
      <a href="../index.html" class="logo d-flex align-items-center">
        <img src="../assets/images/Logo-new.png" alt="logo">
      </a>
      <nav id="navbar" class="navbar">
        <ul>
          <li><a href="../index.html" class="">Home</a></li>
          <li><a href="../services.html" class="">Services</a></li>
          <li><a href="../portfolio.html" class="">Portfolio</a></li>
          <li><a href="../testimonials.html" class="">Testimonials</a></li>
          <!-- <li><a href="team.html" class="">Team</a></li> -->
          <li class="dropdown"><a href="#"><span>Menu</span> <i class="bi bi-chevron-down dropdown-indicator"></i></a>
            <ul>
              <li><a href="../about.html">About</a></li>
              <li><a href="../faqs.html">FAQs</a></li>
              <li><a href="../privacy-policy.html">Privacy Policy</a></li>
            </ul>
          </li>
          <li><a href="../blogs.html">Blogs</a></li>
        </ul>
      </nav><!-- .navbar -->
      <a href="../contact.html" class="btn-get-started hide-on-mobile">Get Quotes</a>
      <button id="darkmode-button"><i class="bi bi-moon-fill"></i></button>
      <i class="mobile-nav-toggle mobile-nav-show bi bi-list"></i>
      <i class="mobile-nav-toggle mobile-nav-hide d-none bi bi-x"></i>
    </div>
  </header>

  <div class="breadcrumbs">
    <div class="page-header d-flex align-items-center">
      <div class="container position-relative">
        <div class="row d-flex justify-content-center">
          <div class="col-lg-6 text-center">
            <h2>{title}</h2>
            <p>{description}</p>
          </div>
        </div>
      </div>
    </div>
    <nav>
      <div class="container">
        <ol>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../blogs.html">Our Blogs</a></li>
          <li>{title}</li>
        </ol>
      </div>
    </nav>
  </div>
  <!-- End Breadcrumbs -->
  
  <!-- Blog Content -->
<main id="main">
 <section class="section">
   <div class="container">
     <!-- Blog Post Title -->
     <h2 style="font-size: 2rem; font-weight: 500; color: var(--color-primary); margin-bottom: 1.5rem;">
       {title}
     </h2>

     <!-- Post Meta -->
     <div class="post-meta mb-4">
       <p style="color: var(--text-grey-color); font-size: 0.95rem;">
         By {author} - <time datetime="{date}">{date}</time>
       </p>
     </div>

     <!-- Featured Image -->
     <div class="mb-4">
       <img src="{image_path}" 
            class="img-fluid rounded-4" 
            alt="{title}"
            style="width: 100%; height: auto;">
     </div>

     <!-- Post Content -->
     <div style="color: var(--text-color); line-height: 1.8;">
       {content}
     </div>
   </div>
 </section>
</main>

  <!-- Footer -->
  <footer id="footer" class="footer-section">
    <div class="container">
      <div class="footer-content pt-5 pb-5">
        <div class="row">
          <div class="col-xl-4 col-lg-4 mb-50">
            <div class="footer-widget">
              <div class="footer-logo">
                <a href="../index.html" class="logo d-flex align-items-center">
                  <img src="../assets/images/Logo-new-2.png" alt="logo">
                </a>
              </div>
              <div class="footer-text">
                <p>BITS India specializes in delivering cutting-edge technology solutions across various domains, including application design, web development, surveillance, AI, cybersecurity, IoT, and smart systems. Our mission is to empower businesses with innovative tools and strategies that drive growth, efficiency, and security.
                </p>
              </div>

              <div class="footer-social-icon">
                <!-- <span>Follow us</span> -->
                <a href="https://www.linkedin.com/in/bits-india/" target="_blank" class="linkedin"><i class="bi bi-linkedin"></i></a>
              </div>

            </div>
          </div>
                
                <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                      <div class="service-widget footer-widget">
                        <div class="footer-widget-heading">
                            <h3>Services</h3>
                        </div>
                          <ul class="list">
                              <li><a href="portfolio.html#all" class="filter-active">All</a></li>
                              <li><a href="portfolio.html#application-design">Application Design</a></li>
                              <li><a href="portfolio.html#web-designing">Web Designing</a></li>
                              <li><a href="portfolio.html#surveillance-solutions">Surveillance Solutions</a></li>
                              <li><a href="portfolio.html#ai-solutions">AI Solutions</a></li>
                              <li><a href="portfolio.html#cybersecurity-solutions">Cybersecurity Solutions</a></li>
                              <li><a href="portfolio.html#iot-smart-systems">IoT and Smart Systems</a></li>
                              <li><a href="portfolio.html#ui-ux-designs">UI/UX Designs</a></li>
                          </ul>
                      </div>
                  </div>
                  <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                      <div class="service-widget footer-widget">
                        <div class="footer-widget-heading">
                            <h3>Information</h3>
                        </div>
                          <ul class="list">
                            <li><a href="about.html">About</a></li>
                            <li><a href="porfolio.html">Portfolio</a></li>
                            <li><a href="faq.html">FAQs</a></li>
                            <li><a href="blogs.html">Blogs</a></li>
                            <li><a href="privacy-policy.html">Privacy Policy</a></li>
                          </ul>
                      </div>
                  </div>
                <div class="col-xl-4 col-lg-4 col-md-6 mb-50">
                    <div class="contact-widget footer-widget">
                        <div class="footer-widget-heading">
                            <h3>Contacts</h3>
                        </div>
                          <div class="footer-text">
                              <p><i class="bi bi-geo-alt-fill mr-15"></i> Shop No 10, Unity Splendour, Salunke Vihar Rd, Wanowrie, Pune, Maharashtra 411040</p>
                              <p><i class="bi bi-telephone-inbound-fill mr-15"></i> +1 1234 56 789</p>
                              <p><i class="bi bi-envelope-fill mr-15"></i> contact@bitsindia.in</p>
                          </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-6 col-lg-6 text-left text-lg-left">
                    <div class="copyright-text">
                        <p>BITS India © 2024</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </footer>
</body>
</html>
"""

        # Write to file
        with open(output_file, 'w') as f:
            f.write(html_content)
        print(f"Created: {output_file}")

# JSON input file
json_input_file = "blogs.json"

# Run the function
generate_blogs_from_json(json_input_file)