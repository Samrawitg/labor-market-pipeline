-- Average unemployment by industry
SELECT industry, 
    ROUND(AVG(unemployment_rate_bls::numeric), 2) as avg_unemployment
FROM combined_labor
GROUP BY industry
ORDER BY avg_unemployment DESC;

-- Top 10 highest paying occupations
SELECT occ_title, 
    a_median as annual_median_wage,
    tot_emp as total_employed
FROM occupational_wages
ORDER BY a_median DESC
LIMIT 10;

-- Data and analyst roles by wage
SELECT occ_title,
    a_median as annual_median_wage,
    tot_emp as total_employed
FROM occupational_wages
WHERE occ_title ILIKE '%data%'
   OR occ_title ILIKE '%business analyst%'
   OR occ_title ILIKE '%operations analyst%'
ORDER BY a_median DESC;

-- Industry summary with unemployment, wages and job openings
SELECT 
    cl.industry,
    ROUND(AVG(cl.unemployment_rate_bls::numeric), 2) as avg_unemployment,
    ROUND(AVG(cl.avg_hourly_earnings::numeric), 2) as avg_hourly_wage,
    ROUND(AVG(cl."JOLTS_openings"::numeric), 0) as avg_job_openings
FROM combined_labor cl
GROUP BY cl.industry
ORDER BY avg_unemployment DESC;