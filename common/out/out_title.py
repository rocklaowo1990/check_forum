import data
import service


def out_title(
    w_i: int,
    len_w: int,
    w_name: str,
    sheet: data.Sheet,
    s_i: int,
    r_i: int,
    len_s: int,
    log_path: str,
):

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 帖子的标题: %s' % (
        w_i + 1,
        len_w,
        w_name,
        sheet.name,
        s_i + 1,
        len_s,
        sheet.data[r_i].title,
    )
    service.c_log(log_content, log_path)

    log_content = '任务[%d/%d] > %s > %s[%d/%d] ==> 帖子的昵称: %s' % (
        w_i + 1,
        len_w,
        w_name,
        sheet.name,
        s_i + 1,
        len_s,
        sheet.data[r_i].nick_name,
    )
    service.c_log(log_content, log_path)
