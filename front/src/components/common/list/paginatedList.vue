<template>
    <div>
        <table>
            <tr>
                <th>No.</th>
                <th>content</th>
                <th>date</th>
                <th>time</th>
            </tr>
            <tr v-for="p in paginatedData" :key="p.id">
                <td>{{ p.id }}</td>
                <td>{{ p.content }}</td>
                <td>{{ p.date }}</td>
                <td>{{ p.time }}</td>
            </tr>
        </table>
        <div class="btn-cover">
            <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
                이전
            </button>
            <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
            <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
                다음
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'posting-list',
    data () {
        return {
            pageNum: 0
        }
    },
    props: {
        // list props 받아서 페이지네이션...
        listArray: {
            type: Array,
            required: true
        },
        pageSize: {
            type: Number,
            required: false,
            default: 10
        }
    },
    methods: {
        nextPage () {
            this.pageNum += 1
        },
        prevPage () {
            this.pageNum -= 1
        }
    },
    computed: {
        pageCount () {
            let listLen = this.listArray.length,
            listSize = this.pageSize,
            page = Math.floor(listLen / listSize)

            if (listLen % listSize > 0) page += 1

            return page
        },
        paginatedData () {
            const start = this.pageNum * this.pageSize,
            end = start + this.pageSize
            return this.listArray.slice(start, end)
        }
    }
}
</script>