'use strict';

console.log('\'Allo \'Allo! Popup');


var $myBundleButton = $('#add-to-bundle');
var $bundleButton = $('#bundle-tab');

var $bundles = $('#existing-bundles-container');
var $myBundles = $('#my-bundle-container');

$myBundles.addClass('hide');

console.log($myBundles);

$myBundleButton.on('click', function(){
  $myBundles.removeClass('hide');
  $bundles.addClass('hide');
  $('.add-to-bundle-container').addClass('hide');
});

$bundleButton.on('click', function(){
  $myBundles.addClass('hide');
  $bundles.removeClass('hide');
});