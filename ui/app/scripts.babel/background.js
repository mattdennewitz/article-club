'use strict';

window.currentData = {};

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if(tab.status !== 'complete' || !tab.url.startsWith('http')) {
        return;
    }

    $.ajax({
        url: 'http://localhost:8000/api/v1/bundles/search/',
        method: 'GET',
        dataType: 'json',
        data: {
            url: tab.url,
            comfort_level: 0
        }
    }).success(function(response) {
        var badge = {text: ''};

        if(response && response.length > 0) {
            badge.text = response.length.toString();
        }

        chrome.browserAction.setBadgeText(badge);

        window.currentData[tabId] = response;
        chrome.runtime.sendMessage({type: 'NEW_DATA', data: response});
    });
});

chrome.tabs.onActivated.addListener(function(tabId, windowId) {
    var dataForTab = window.currentData[tabId];

    var badgeText = (!!dataForTab) ? dataForTab.length : 0;

    chrome.browserAction.setBadgeText({text: badgeText.toString()});
    chrome.runtime.sendMessage({type: 'NEW_DATA', data: dataForTab});
});
