'use strict';

console.log('\'Allo \'Allo! Popup');

var $myBundleButton = $('#my-bundle-tab');
var $bundleButton = $('#bundle-tab');

var $bundles = $('#existing-bundles-container');
var $myBundles = $('#my-bundle-container');

$myBundles.addClass('hide');

console.log($myBundles);

$myBundleButton.on('click', function () {
  $myBundles.removeClass('hide');
  $bundles.addClass('hide');
});

$bundleButton.on('click', function () {
  $myBundles.addClass('hide');
  $bundles.removeClass('hide');
});
//# sourceMappingURL=popup.js.map
