const CACHE = 'cache_visupdt1';
const filestoCache = [
                      '/static/style/base.css',
                      '/static/assets/img/favicon.png',
                      '/static/assets/img/bg.jpeg',
                      '/static/assets/vendor/icofont/icofont.min.css',
                      '/static/assets/vendor/boxicons/css/boxicons.min.css',
                      '/static/assets/vendor/venobox/venobox.css',
                      '/static/assets/vendor/jquery/jquery.min.js',
                      '/static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js',
                      '/static/assets/vendor/jquery.easing/jquery.easing.min.js',
                      '/static/assets/vendor/isotope-layout/isotope.pkgd.min.js',
                      '/static/assets/vendor/venobox/venobox.min.js',
                      ]

self.addEventListener('install', function(event) {
  console.log('The service worker is being installed.');
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE).then(function(cache) {
      
      return cache.addAll(filestoCache);
    })
  );
});


self.addEventListener('activate', (e) => {
  self.skipWaiting();

  e.waitUntil(
    caches.keys().then((keyList) => {
          return Promise.all(keyList.map((key) => {
        if(key !== CACHE) {
          return caches.delete(key);
        }
      }));
    })
  );
});

self.addEventListener('fetch', function(event) {

     event.respondWith(
      caches.match(event.request).then(response => {
        if (response) {
          console.log('Found ', event.request.url, ' in cache');
          return response;
        }
        console.log('Network request for ', event.request.url);
        return fetch(event.request)

      }).catch(function(err) {
        // Fallback to cache
        console.log("Oh Snap :" + err);
    })
    );
});

