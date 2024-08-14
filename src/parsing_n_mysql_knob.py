import pandas as pd

# CSV 파일 불러오기
file_path = '/Users/yoonji_kim/delab/tuning/parsing_mysql_parameter/mysql_parameters.csv'
df = pd.read_csv(file_path)

# Knob 리스트
knobs = [
    "innodb_buffer_pool_size", "innodb_log_file_size", "innodb_log_buffer_size",
    "innodb_flush_log_at_trx_commit", "innodb_flush_method", "innodb_io_capacity",
    "innodb_max_dirty_pages_pct", "innodb_file_per_table", "innodb_read_io_threads",
    "innodb_write_io_threads", "query_cache_size", "query_cache_type",
    "max_connections", "table_open_cache", "thread_cache_size", "tmp_table_size",
    "max_heap_table_size", "join_buffer_size", "sort_buffer_size", "read_buffer_size",
    "read_rnd_buffer_size", "key_buffer_size", "bulk_insert_buffer_size",
    "innodb_thread_concurrency", "innodb_adaptive_hash_index", "innodb_flush_neighbors",
    "innodb_lru_scan_depth", "innodb_old_blocks_pct", "innodb_old_blocks_time",
    "innodb_purge_threads", "max_allowed_packet", "transaction_allow_block_size",
    "max_heap_table_size", "innodb_online_alter_log_max_size", "key_cache_age_threshold",
    "binlog_cache_size", "innodb_sort_buffer_size"
]

# 언더스코어(_)를 하이픈(-)으로 변경
knobs_with_hyphens = [knob.replace("_", "-") for knob in knobs]

# 매칭된 결과 저장할 리스트
matching_results = []

# 모든 파라미터와 비교
for knob in knobs_with_hyphens:
    matches = df[df['Parameter'].str.contains(knob, case=False, na=False)]
    if not matches.empty:
        matching_results.append(matches)

# 매칭된 결과를 데이터프레임으로 변환
df_results = pd.concat(matching_results)

# 결과를 CSV 파일로 저장
output_file_path = '/Users/yoonji_kim/delab/tuning/parsing_mysql_parameter/csv/mysql_parameters_using_lasso.csv'
df_results.to_csv(output_file_path, index=False)

print(f"Matching results saved to {output_file_path}")
