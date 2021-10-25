var dataCount = 0;
var CHUNK_COUNT = 230;
// var chartDom = document.getElementById('main');
var myChart = echarts.init(document.getElementById('main'));
//https://blog.openstreetmap.org/2012/04/01/bulk-gps-point-data/
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
//        data = [98.986404, 30.301999,
//              98.992788, 30.284671,
//              98.976531, 30.260165,
//              98.981092, 30.253656,
//              98.981226, 30.235071,
//              98.999207, 30.220594,
//              99.000722, 30.216161,
//              98.990861, 30.200213,];
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
