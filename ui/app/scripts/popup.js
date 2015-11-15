'use strict'

// ---

;
function renderPage(data) {
    var $b = $('#bundles');
    $b.empty();

    var $bundleTitle = $('.bundle-title');
    var $bundleTopic = $('.bundle-topic-name');
    var $bundleCurator = $('.bundle-curator');

    var $myBundles = $('.my-bundles');

    var $link = $('.bundle-link');

    for (var i in data) {
        var bundle = data[i];
        var el = $('<li>' + bundle.title + '</li>');

        $bundleCurator.html(bundle.curator);
        $bundleTitle.html(bundle.title);
        $bundleTopic.html(bundle.title);
        $myBundles.append('<li class="bundle"><p class="my-bundle-item">' + bundle.title + '<i class="add-button fa fa-plus-circle"></i></p></li>');

        for (var l in bundle.link_list) {
            var link = bundle.link_list[l];

            $link.append('<li class="bundle-link"><a class="linkurl urlname" href="' + link.link.url + '">' + link.link.title + '</a><span class="comfort-level"><i class="fa fa-circle comfort-' + link.comfort_level + '"></i></span></li>');
            console.log(link);

            // linksContainer.append(
            //     $('<li><a href="' + link.link.url + '">' + link.link.title + '</a></li>')
            // );
        }

        // append list of links to parent bundle <ul>
        // el.append(linksContainer);

        // add bundle card to popup list
        $b.append(el);
    }
}

// poll for data from cache store
function pollData() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (arrayOfTabs) {
        var tabId = arrayOfTabs[0].id;
        chrome.runtime.getBackgroundPage(function (page) {
            renderPage(page.currentData[tabId]);
        });
    });
}

chrome.runtime.onMessage.addListener(function (msg) {
    if (msg.type == 'NEW_DATA') {
        pollData();
    }
});

// boot
$(function () {
    pollData();
});

// ---

var $myBundleButton = $('#add-to-bundle');
var $bundleButton = $('#bundle-tab');

var $bundles = $('#existing-bundles-container');
var $myBundles = $('#my-bundle-container');

$myBundles.addClass('hide');

console.log($myBundles);

$myBundleButton.on('click', function () {
    $myBundles.removeClass('hide');
    $bundles.addClass('hide');
    $('.add-to-bundle-container').addClass('hide');
});

$bundleButton.on('click', function () {
    $myBundles.addClass('hide');
    $bundles.removeClass('hide');
});
//# sourceMappingURL=popup.js.map
