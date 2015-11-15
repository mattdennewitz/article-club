'use strict';

// ---

function renderPage(data) {
    var $b = $('#bundles');
    $b.empty();

    for(var i in data) {
        var bundle = data[i];
        var el = $('<li>' + bundle.title + '</li>');

        var linksContainer = $('<ul></ul>');

        for(var l in bundle.link_list) {
            var link = bundle.link_list[l];

            linksContainer.append(
                $('<li><a href="' + link.link.url + '">' + link.link.title + '</a></li>')
            );
        }

        // append list of links to parent bundle <ul>
        el.append(linksContainer);

        // add bundle card to popup list
        $b.append(el);
    }
}

// poll for data from cache store
function pollData() {
    chrome.tabs.query({active: true, currentWindow: true}, function(arrayOfTabs) {
        var tabId = arrayOfTabs[0].id;
        chrome.runtime.getBackgroundPage(function(page) {
            renderPage(page.currentData[tabId]);
        });
    });
}

chrome.runtime.onMessage.addListener(function(msg) {
    if(msg.type == 'NEW_DATA') {
        pollData();
    }
})

// boot
$(function() {
    pollData()
});

// ---


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
