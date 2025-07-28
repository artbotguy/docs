   SWIPER
    - ошибка стилей с огромным слайдером: 
        для .swiper:
            width: 100%;
        для родительского узла стили:
            width: 100%; // [optional]
            max-width: 100%; // [optional] 
            min-height: 0;  // [optional]
            min-width: 0;  // for swiper corretly showing
            :::
        а также для вертикального слайдера - указывается автовысота

    - не работает какая-либо логика
        проверить, подключен ли соответвующий модульы

    - не работают thumbs
        вместо объявления из demo предлагается использовать:
        let thumbsSwiper = ref(null)
        function setThumbsSwiper (swiper) {
            thumbsSwiper.value = swiper
        }
    - свайпер и не только. длина изображения с динамическим размером
        задача width родительскому элемену важна - нужно проверить цепочку родителей
        и задать длину каждому. (например, node <swiper></swiper>)

    - установка одинаковой высоты слайдов
        .swiper-slide {
            height: auto;
        }
