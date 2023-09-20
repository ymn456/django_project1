import copy

from django.utils.safestring import mark_safe


class pagination(object):
    def __init__(self,request,queryset, pages_show = 5, size_one_page = 4):
        self.request = request
        self.queryset = queryset
        self.pages_show = pages_show
        self.size_one_page = size_one_page

    def html(self):

        page = self.request.GET.get("page", "1")
        if page.isdecimal():
            page = int(page)


        start = (page - 1) * self.size_one_page
        end = page * self.size_one_page

        query_count = self.queryset.count()
        pages_count, last_page_size = divmod(query_count, self.size_one_page)


        one_side = int((self.pages_show - 1) / 2)
        if last_page_size > 0:
            pages_count += 1

        if page - one_side <= 0:
            start_num = 1
            end_num = min(start_num + self.pages_show - 1, pages_count)
        elif page + one_side >= pages_count:
            end_num = pages_count
            start_num = max(pages_count - self.pages_show+1, 1)
        else:
            start_num = int(page - one_side)
            end_num = int(page + one_side)

        page_string_list = []

        # 上一页
        if page > 1:
            prev = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
        else:
            prev = '<li><a href="?page={}">上一页</a></li>'.format(page)
        page_string_list.append(prev)

        # 页码
        for i in range(start_num, end_num + 1):
            ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
            page_string_list.append(ele)

        # 下一页
        if page < pages_count:
            prev = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
        else:
            prev = '<li><a href="?page={}">下一页</a></li>'.format(page)
        page_string_list.append(prev)

        # 跳转
        search_page = \
            """
            <div style="float:right;width:100px;">
                <form method="get"  >
                    <div class="input-group">
                        <input type="text" name="page" class="form-control" placeholder="页码">
                        <span class="input-group-btn">
                            <button class="btn btn-default" type="submit">跳转</button>
                        </span>
                    </div><!-- /input-group -->
                </form>
            </div>
            """
        page_string_list.append(search_page)
        page_string = mark_safe(''.join(page_string_list))

        self.queryset =self.queryset[start:end]

        return page_string, self.queryset