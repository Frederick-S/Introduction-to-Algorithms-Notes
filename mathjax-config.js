window.MathJax = {
    tex: {
        inlineMath: [
            ['$', '$']
        ],
        displayMath: [
            ['$$', '$$']
        ],
        autoload: {
            color: [],
            colorV2: ['color']
        },
        packages: {
            '[+]': ['noerrors']
        }
    },
    options: {
        ignoreHtmlClass: 'tex2jax_ignore',
        processHtmlClass: 'tex2jax_process'
    },
    loader: {
        load: ['[tex]/noerrors']
    }
}
