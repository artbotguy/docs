references:
    - webpack

Варианты импорта:
    Кейс LODASH-ES:
        попытка импотртировать в проекте WV в стиле 
            import {cloneDeep} from 'lodash-es' закончилась неудачей
        однако получилось
            import cloneDeep from 'lodash-es/cloneDeep'