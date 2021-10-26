var dataCount = 0;
var CHUNK_COUNT = 230;
var myChart = echarts.init(document.getElementById('main'));
function fetchData(idx){
    if (idx >= CHUNK_COUNT){
      return;
    }
    var ROOT_PATH =
    'https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples';
    var dataURL = ROOT_PATH + '/data/asset/data/gps/gps_' + idx + '.bin';
    var xhr = new XMLHttpRequest();
    xhr.open('GET', dataURL, true);
    xhr.responseType = 'arraybuffer';
    xhr.onload = function (e){
        var data = new Float32Array(3710);
        var obj = eval('({{result_json|safe }})')
        data = obj['a']
        myChart.appendData({
        seriesIndex: 0,
        data: data
        });
        console.log(data);
        // fetchData(idx + 1);
    };
    xhr.send();
}
var option = {
    backgroundColor: '#000',
    title: {
        text: 'ComicMap',
        left: 'center',
        textStyle: {
            color: '#fff'
        }
    },
    geo: {
        map: 'china',
        roam: true,
        label: {
            emphasis: {
                show: false
            }
        },
        silent: true,
        itemStyle: {
            normal: {
                areaColor: '#323c48',
                borderColor: '#111'
            },
        emphasis: {
            areaColor: '#2a333d'
            }
        }
    },
    series: [{
        name: '弱',
        type: 'scatterGL',
        progressive: 1e6,
        coordinateSystem: 'geo',
        symbolSize: 5,
        zoomScale: 0.002,
        blendMode: 'lighter',
        large: true,
        itemStyle: {
            color: 'rgb(20, 15, 2)'
        },
        postEffect: {
            enable: true
        },
        silent: true,
        dimensions: ['lng', 'lat'],
        data: new Float32Array()
        }
    ]
};

fetchData(0);
myChart.setOption(option);
