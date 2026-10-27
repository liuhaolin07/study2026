# -*- coding: utf-8 -*-
"""解压课件/真题到 site/assets，并生成文件清单 assets_manifest.json。"""
import zipfile, os, json, shutil, re

REF = r"D:\File\OneDrive\Desktop\code\Algorithms\参考"
SITE = r"D:\File\OneDrive\Desktop\code\Algorithms\site"
ASSETS = os.path.join(SITE, "assets")

# (zip 文件名, 目标目录)
EXTRACT = [
    ("1. 【C++篇】C++编程课_课件【目录版】.zip", "courses/cpp"),
    ("4. 【数据结构篇】《数据结构》课件【目录版】.zip", "courses/ds"),
    ("5. 【数据结构篇】数据结构课堂代码.zip", "courses/ds-code"),
    ("6. 【算法基础篇】算法基础课件【目录版】.zip", "courses/basic"),
    ("7. 【算巩固篇】算法巩固课件【目录版】.zip", "courses/consolidate"),
    ("8. 【算法提高篇】算法提高课件【加目录版】.zip", "courses/advanced"),
    ("10. 【真题篇】蓝桥杯国赛真题及详细解析.zip", "exams/national"),
    ("11. 【真题篇】蓝桥杯省赛真题及详细解析.zip", "exams/provincial"),
    ("9. 【真题篇】蓝桥杯历年真题.zip", "exams/history"),
]

def fix_name(info):
    """zip 内中文文件名：无 utf8 标志时按 cp437->gbk 修复。"""
    name = info.filename
    if info.flag_bits & 0x800:
        return name
    try:
        return name.encode("cp437").decode("gbk")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return name

def strip_top(names):
    """去掉压缩包内冗余的顶层目录（可能嵌套两层同名目录）。"""
    prefix_parts = None
    for n in names:
        parts = n.split("/")
        if len(parts) <= 1:
            return None
        p = parts[0]
        if prefix_parts is None:
            prefix_parts = p
        elif prefix_parts != p:
            return None
    # 只剩一个顶层目录才剥离
    dirs = set(n.split("/")[0] for n in names)
    if len(dirs) == 1 and prefix_parts:
        return prefix_parts + "/"
    return None

def extract_zip(zip_path, dest):
    os.makedirs(dest, exist_ok=True)
    with zipfile.ZipFile(zip_path) as z:
        infos = [i for i in z.infolist() if not i.is_dir()]
        names = [fix_name(i) for i in infos]
        prefix = strip_top(names)
        n = 0
        for info, name in zip(infos, names):
            rel = name[len(prefix):] if prefix and name.startswith(prefix) else name
            if not rel or rel.startswith(".."):
                continue
            # 历年真题里有些课件类文件不重要，全部保留
            target = os.path.join(dest, *rel.split("/"))
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with z.open(info) as src, open(target, "wb") as out:
                shutil.copyfileobj(src, out)
            n += 1
    return n

def main():
    manifest = {}
    for zip_name, rel_dest in EXTRACT:
        dest = os.path.join(ASSETS, rel_dest.replace("/", os.sep))
        if os.path.exists(dest):
            cnt = sum(len(fs) for _, _, fs in os.walk(dest))
            print(f"skip (exists): {rel_dest} ({cnt} files)")
        else:
            cnt = extract_zip(os.path.join(REF, zip_name), dest)
            print(f"extracted {zip_name} -> {rel_dest}: {cnt} files")
        manifest[rel_dest] = zip_name

    # 路线图 PNG
    road_src = os.path.join(REF, "路线")
    road_dst = os.path.join(ASSETS, "roadmap")
    os.makedirs(road_dst, exist_ok=True)
    for f in os.listdir(road_src):
        if f.endswith(".png"):
            shutil.copy2(os.path.join(road_src, f), os.path.join(road_dst, f))
    print("roadmap images copied:", len([f for f in os.listdir(road_dst)]))

    # 学习指南
    guide = os.path.join(ASSETS, "guide", "算法竞赛课程学习指南.pdf")
    if not os.path.exists(guide):
        os.makedirs(os.path.dirname(guide), exist_ok=True)
        shutil.copy2(os.path.join(REF, "0. 算法竞赛课程学习指南.pdf"), guide)
    print("guide copied")

    with open(os.path.join(SITE, "data", "assets_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("manifest saved")

if __name__ == "__main__":
    main()
