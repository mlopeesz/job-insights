from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    jobs_types = set()
    for job in jobs_list:
        jobs_types.add(job["job_type"])
    return list(jobs_types)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [job for job in jobs if (job["job_type"] == job_type)]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    jobs_by_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    salaries_list = [
        int(job["max_salary"])
        for job in jobs_list
        if job["max_salary"].isnumeric()
    ]
    return max(salaries_list)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    salaries_list = [
        int(job["min_salary"])
        for job in jobs_list
        if job["min_salary"].isnumeric()
    ]
    return min(salaries_list)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('"min_salary" and "max_salary" required')

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError('"min_salary" and "max_salary" must be integers')

    if job["min_salary"] > job["max_salary"]:
        raise ValueError('"min_salary" is greater than "max_salary"')

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary_range.append(job)
        except Exception:
            print("An exception occurred")
    return jobs_by_salary_range
