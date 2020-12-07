#coding=utf-8
def check_res(res, check):
    '''检验返回结果和预期是否一致'''
    res = res.replace('":"', '=').replace('":', '=').replace(',','，')
    # 将返回结果进行修改，以便于与预期结果比较
    for i in check.split(','):  # 预期结果以‘，’号分开
        # print(i)
        if i not in res:
            print('校验失败，预期结果：%s，实际结果：%s'%(i,res))
            return False
            # 几个预期结果有一个不满足就是失败，必须全满足才是成功
    print('校验成功，实际结果为：%s'%res)
    return True