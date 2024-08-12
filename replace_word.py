import os

import cfg


old_word = ""
new_word = ""
replace_mode = False


def process(srt_dir, do_replace=replace_mode):
    count = 0
    for dir_path, _, file_names in os.walk(srt_dir):
        for file_name in file_names:
            if file_name.endswith(cfg.output_srt_suffix):
                srt_file = os.path.join(dir_path, file_name)
                with open(srt_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines, 1):
                        if old_word in line:
                            count += line.count(old_word)
                            print(f"{file_name}, Line {i}: {line.strip()}")
                if do_replace:
                    with open(srt_file, "r", encoding="utf-8") as f:
                        content = f.read()
                        content = content.replace(old_word, new_word)
                    with open(srt_file, "w", encoding="utf-8") as f:
                        f.write(content)
    if do_replace:
        print(f"{cfg.single_enter}Count of words having been replaced: {count}")
    else:
        print(f"{cfg.single_enter}Count of words that can be replaced: {count}")


if __name__ == "__main__":
    process(cfg.output_dir)
