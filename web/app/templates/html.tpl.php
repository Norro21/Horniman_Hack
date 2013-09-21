<!DOCTYPE html>
<!--[if IE 8]>         <html class="no-js lt-ie9" lang="en" > <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title><?php print $page_title; ?></title>
  <link rel="stylesheet" href="/css/foundation.css">
  <script src="/js/vendor/custom.modernizr.js"></script>
</head>
<body>

  <div class="row">
    <div class="large-12 columns">
      <h1><?php print $page_title; ?></h1>
    </div>
  </div>


  <div class="row">
    <div class="large-12 columns">
      <?php print $content; ?>
    </div>
  </div>



  <?php if (!empty($debug)): ?>
    <?php print $debug; ?>
  <?php endif; ?>

</body>
</html>