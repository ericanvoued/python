function xhrGetScript(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("get", url, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            if (xhr.status >= 200 && xhr.status < 300 || xhr.status == 304) {
                var script = document.createElement("script");
                script.type = text / javascript;
                script.text = xhr.responseText;
                document.body.appendChild(script);
            }
        }
    }
}

