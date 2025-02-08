document.addEventListener('DOMContentLoaded', function() {
    new Vue({
        el: '#app',
        data: {
            rawRule: '',
            formattedResult: '',
            unformatRawRule: '',
            unformattedResult: '',
            hexEncodeInput: '',
            hexEncodeResult: '',
            hexToStrInput: '',
            hexToStrResult: '',
            unicodeInput: '',
            unicodeResult: '',
            unicodeFlag: 'encode',
            encodeToHexInput: '',
            encodeToHexResult: '',
            encodeToHexFlag: 'e',
            countTimeInput: '',
            countTimeResult: '',
            countTimeSeconds: 60,
            countSubTimeInput1: '',
            countSubTimeInput2: '',
            countSubTimeResult: '',
            googleQuery: '',
            googleSiteFilters: '',
            googleSearchResult: ''
        },
        methods: {
            hexEncode: function() {
                const rawString = this.hexEncodeInput;
                fetch('/api/hexencode', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ raw_string: rawString })
                })
                .then(response => response.json())
                .then(data => {
                    this.hexEncodeResult = data.result;
                })
                .catch(error => {
                    console.error('Hex编码请求失败:', error);
                    alert('Hex编码请求失败，请检查输入或联系管理员。');
                });
            },
            hexToStr: function() {
                const rawString = this.hexToStrInput;
                fetch('/api/hextostr', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ raw_string: rawString })
                })
                .then(response => response.json())
                .then(data => {
                    this.hexToStrResult = data.result;
                })
                .catch(error => {
                    console.error('Hex转字符串请求失败:', error);
                    alert('Hex转字符串请求失败，请检查输入或联系管理员。');
                });
            },
            unicodeEncodeDecode: function() {
                const rawString = this.unicodeInput;
                const flag = this.unicodeFlag;
                const url = flag === 'encode' ? '/api/tounicode' : '/api/fromunicode';
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ raw_string: rawString })
                })
                .then(response => response.json())
                .then(data => {
                    this.unicodeResult = data.result;
                })
                .catch(error => {
                    console.error('Unicode编码/解码请求失败:', error);
                    alert('Unicode编码/解码请求失败，请检查输入或联系管理员。');
                });
            },
            encodeToHex: function() {
                const rawString = this.encodeToHexInput;
                const flag = this.encodeToHexFlag;
                fetch('/api/encode_to_hex', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ raw_string: rawString, flag: flag })
                })
                .then(response => response.json())
                .then(data => {
                    this.encodeToHexResult = data.result;
                })
                .catch(error => {
                    console.error('编码到Hex请求失败:', error);
                    alert('编码到Hex请求失败，请检查输入或联系管理员。');
                });
            },
            countTime: function() {
                const timeStr = this.countTimeInput;
                const secondsToAdd = this.countTimeSeconds;
                fetch('/api/counttime', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ time_str: timeStr, seconds_to_add: secondsToAdd })
                })
                .then(response => response.json())
                .then(data => {
                    this.countTimeResult = data.result;
                })
                .catch(error => {
                    console.error('计算时间请求失败:', error);
                    alert('计算时间请求失败，请检查输入或联系管理员。');
                });
            },
            countSubTime: function() {
                const timeStr1 = this.countSubTimeInput1;
                const timeStr2 = this.countSubTimeInput2;
                fetch('/api/countsubtime', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ time_str1: timeStr1, time_str2: timeStr2 })
                })
                .then(response => response.json())
                .then(data => {
                    this.countSubTimeResult = data.result;
                })
                .catch(error => {
                    console.error('计算时间差请求失败:', error);
                    alert('计算时间差请求失败，请检查输入或联系管理员。');
                });
            },
            googleSearch: function() {
                const query = this.googleQuery;
                const siteFilters = this.googleSiteFilters;
                fetch('/api/google_search', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ query: query, site_filters: siteFilters })
                })
                .then(response => response.json())
                .then(data => {
                    this.googleSearchResult = data.search_url;
                })
                .catch(error => {
                    console.error('Google搜索请求失败:', error);
                    alert('Google搜索请求失败，请检查输入或联系管理员。');
                });
            },
            formatRule: function() {
                const rawRule = this.rawRule;
                fetch('/api/format', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ raw_rule: rawRule })
                })
                .then(response => response.json())
                .then(data => {
                    this.formattedResult = data.result;
                    this.$nextTick(() => {
                        this.adjustTextareaHeight(document.getElementById('result'));
                    });
                })
                .catch(error => {
                    console.error('格式化请求失败:', error);
                    alert('格式化请求失败，请检查输入或联系管理员。');
                });
            },
            unformatRule: function() {
                const rawRule = this.unformatRawRule;
                fetch('/api/unformat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ raw_rule: rawRule })
                })
                .then(response => response.json())
                .then(data => {
                    this.unformattedResult = data.result;
                    this.$nextTick(() => {
                        this.adjustTextareaHeight(document.getElementById('unformat-result'));
                    });
                })
                .catch(error => {
                    console.error('反格式化请求失败:', error);
                    alert('反格式化请求失败，请检查输入或联系管理员。');
                });
            },
            adjustTextareaHeight: function(textarea) {
                textarea.style.height = 'auto';
                textarea.style.height = textarea.scrollHeight + 'px';
            }
        },
        watch: {
            rawRule: function() {
                this.formatRule();
            },
            unformatRawRule: function() {
                this.unformatRule();
            },
            hexEncodeInput: function() {
                this.hexEncode();
            },
            hexToStrInput: function() {
                this.hexToStr();
            },
            unicodeInput: function() {
                this.unicodeEncodeDecode();
            },
            unicodeFlag: function() {
                this.unicodeEncodeDecode();
            },
            encodeToHexInput: function() {
                this.encodeToHex();
            },
            encodeToHexFlag: function() {
                this.encodeToHex();
            },
            countTimeInput: function() {
                this.countTime();
            },
            countSubTimeInput1: function() {
                this.countSubTime();
            },
            countSubTimeInput2: function() {
                this.countSubTime();
            }
        },
        mounted: function() {
            const textareas = document.querySelectorAll('textarea');
            textareas.forEach(textarea => {
                textarea.addEventListener('input', (event) => this.adjustTextareaHeight(event.target));
                this.adjustTextareaHeight(textarea); // Adjust height on load
            });
        }
    });
});