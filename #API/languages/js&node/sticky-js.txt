        ошибка (low), связанная с некорректным отображением липкого элемента - проблема заключалась в 
        некорректном body. который не занимал всю страницу

        if{
        если element.top === 0
        }elseif{
        если элемент должен активным, есть два сценария
        элементу добавляется fixed
        if{
            логика для приклеенного элемента
            работает, когда 
            (
            this.scrollTop + 
            element.sticky.rect.height + 
            element.sticky.marginTop
            ) >
            (
            element.sticky.container.rect.top + 
            element.sticky.container.offsetHeight -     /// высота элемента (body)
            element.sticky.marginBottom
            )
        }else {
            логика до элемента, который уперся
        }
        }else{
        обнуление
        }